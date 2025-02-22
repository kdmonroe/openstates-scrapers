from utils.actions import Rule, BaseCategorizer

rules = (
    Rule(r"Enacted, Chapter", "became-law"),
    Rule(r"Approved by Governor", "executive-signature"),
    Rule(r"Vetoed by Governor", "executive-veto"),
    Rule(r"(House|Senate) sustained Governor's veto", "veto-override-failure"),
    Rule(r"\s*Amendment(s)? .+ agreed", "amendment-passage"),
    Rule(r"\s*Amendment(s)? .+ withdrawn", "amendment-withdrawal"),
    Rule(r"\s*Amendment(s)? .+ rejected", "amendment-failure"),
    Rule(r"Subject matter referred", "referral-committee"),
    Rule(r"Rereferred to", "referral-committee"),
    Rule(r"Referred to", "referral-committee"),
    Rule(r"Assigned ", "referral-committee"),
    Rule(r"Reported from", "committee-passage"),
    Rule(r"Read third time and passed", ["passage", "reading-3"]),
    Rule(r"Read third time and agreed", ["passage", "reading-3"]),
    Rule(r"Passed (Senate|House)", "passage"),
    Rule(r"passed (Senate|House)", "passage"),
    Rule(r"Read third time and defeated", "failure"),
    Rule(r"Presented", "introduction"),
    Rule(r"Prefiled and ordered printed", "introduction"),
    Rule(r"Read first time", "reading-1"),
    Rule(r"Read second time", "reading-2"),
    Rule(r"Read third time", "reading-3"),
    Rule(r"Senators: ", None),
    Rule(r"Delegates: ", None),
    Rule(r"Committee substitute printed", "substitution"),
    Rule(r"Bill text as passed", None),
    Rule(r"Acts of Assembly", None),
    Rule(r"Agreed to by Senate by voice vote", "passage"),
    Rule(r"Agreed to by House by voice vote", "passage"),
    Rule(r"Signed by President", "executive-signature"),
    Rule(r"Signed by Speaker", "executive-signature"),
    Rule(r"Governor's recommendation adopted", "executive-signature"),
    Rule(r"Governor's Action Deadline", "executive-receipt"),
    Rule(r"Enrolled Bill communicated to Governor", "executive-receipt"),
    Rule(r"Governor's recommendation received", "executive-veto-line-item"),
    Rule(r".*requested.*conference committee", "referral-committee"),
    Rule(r"Conferes appointed", "referral-committee"),
    Rule(r".*[Cc]onference report.*agreed", "committee-passage-favorable"),
    Rule(r"rejected Governor", "veto-override-passage"),
    Rule(r".*amendments agreed to.*senate", "amendment-passage"),
    Rule(r".*senate substitute.*agreed", "substitution"),
    Rule(r"intro", "introduction"),
    Rule(r"filed", "filing"),
    Rule(r"[Ee]nrolled", "enrolled"),
    Rule(r"VOTE.*Passage", "passage"),
    Rule(r".*pass.*[Aa]mendment", "amendment-passage"),
    # stop parsing for more rules so we don't match committee-passage-favorable
    Rule(r"^Passed by indefinitely", "deferral", True),
    Rule(r"^Passed by with letter", "deferral", True),
    Rule(r"^Passed.*in.*-Y", "committee-passage-favorable"),
    Rule(r"Failed to report", "committee-failure"),
    Rule(r"failed to recommend reporting", "committee-failure"),
    Rule(r"Failed to pass in", "failure"),
    Rule(r"withdrawn", "withdrawal"),
    Rule(r"reporting with substitute", "substitution"),
    Rule(r"insisted on substitute", "substitution"),
    Rule(r".*substitute.*agree", "substitution"),
    Rule(r"^Engrossed.*committee substitute", "substitution"),
    Rule(r".*[Aa]mendment.*agreed to", "amendment-passage"),
    Rule(r".*[Aa]mendment.*rejected", "amendment-failure"),
    Rule(r"^[Tt]abled", "deferral"),
    Rule(r"refer.*[Cc]ommittee", "referral-committee"),
    Rule(r"[Rr]eferred from", "referral-committee"),
)


class Categorizer(BaseCategorizer):
    rules = rules

    def categorize(self, text):
        attrs = BaseCategorizer.categorize(self, text)
        return attrs
