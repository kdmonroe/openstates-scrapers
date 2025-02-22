import datetime
import json

from openstates.scrape import Scraper, Event

import pytz

from .utils import open_csv


class CTEventScraper(Scraper):

    _tz = pytz.timezone("US/Eastern")

    def __init__(self, *args, **kwargs):
        super(CTEventScraper, self).__init__(*args, **kwargs)

    def scrape(self):
        for (code, name) in self.get_comm_codes():
            yield from self.scrape_committee_events(code, name)

    def scrape_committee_events(self, code, name):
        events_url = (
            "http://www.cga.ct.gov/basin/fullcalendar/commevents.php?"
            f"comm_code={code}"
        )
        event_objects = set()
        events_data = self.get(events_url, verify=False).text
        events = json.loads(events_data)

        DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
        for info in events:
            if not info["title"]:
                self.warning("Event found with no title; it will be skipped")
                continue
            elif info["title"].startswith("CANCELLED:"):
                self.info(
                    "Cancelled event found; it will be skipped: {}".format(
                        info["title"]
                    )
                )
                continue
            when = datetime.datetime.strptime(info["start"], DATETIME_FORMAT)
            event_name = f"{name}#{info['title']}#{when}"
            if event_name in event_objects:
                self.warning(f"Found duplicate event: {event_name}. Skipping")
                continue
            event_objects.add(event_name)
            # end = datetime.datetime.strptime(info['end'], DATETIME_FORMAT)
            where = "{0} {1}".format(info["building"].strip(), info["location"].strip())
            # end_time=self._tz.localize(end),
            event = Event(
                start_date=self._tz.localize(when),
                location_name=where,
                name=info["title"],
                description=info["title"],
            )
            event.add_source(events_url)
            event.add_committee(name)
            event.dedupe_key = event_name

            yield event

    def get_comm_codes(self):
        url = "ftp://ftp.cga.ct.gov/pub/data/committee.csv"
        page = self.get(url)
        page = open_csv(page)
        return [(row["comm_code"].strip(), row["comm_name"].strip()) for row in page]
