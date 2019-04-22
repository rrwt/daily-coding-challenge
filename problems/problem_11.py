"""
Implement an autocomplete system. That is, given a query string s
and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal],
return [deer, deal].
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

words = ["ADOXOGRAPHY", "ADUMBRATE", "AEIPATHY", "AEONIAN", "AESTHETE", "AFFABLE", "AILUROPHILE",
         "AIRNESS", "ALACRITY", "ALIS PROPRIIS VOLAT",
         "BACKPFEIFENGESICHT", "BAILE", "BAKKUSHAN", "BALISTIC", "BASOREXIA", "BAUSNI",
         "BE EXTRAORDINARY", "BE HAPPY", "BEATHA", "BEATIFY",
         "CAFUNE", "CALCINATION", "CALM", "CAMHANAICH", "CANDOR", "CAPRICE", "CARE", "CARPE DIEM",
         "CARPE NOCTEM", "CASCADE", "CASHMERE", "CATHARSIS",
         "DAIL", "DAIMON", "DALISAY", "DALLIANCE", "DANDY", "DATHUIL", "DAUNTLESS", "DAUWTRAPPEN",
         "DAZZLED", "DAZZLING", "DEBONAIR", "DEFENESTRATION",
         "EAGERNESS", "EARNEST", 'EASE', "EASE-OF-MIND", "EBULLIENCE", "EBULLIENT", "ECOSOPHY",
         "ECSTATIFY", "EFFERVESCENCE", "EFFERVESCENT", "EFFLORESCENCE",
         "FABULOUS", "FADO", "FAILEAS", "FAILTE", "FAIR", "FAIRNESS", "FAITH", "FAITHFUL", "FAME",
         "FAMILY", "FAMOUS", "FANAA", "FANCY", "FANTABULOUS",
         "GAEL", "GAIET", "GAISCE", "GAMBOL", "GARGANTUAN", "GEMUTLICHKEIT", "GENERAVITY", "GIDDY",
         "GIFT", "GIGGLING", "GIGIL", "GINGER", "GLAD", "GLAMOR",
         "HABIBI", "HABILIN", "HALAKHAK", "HALCYON", "HALO", "HANDSOME", "HANYAUKU", "HAPPINESS",
         "HAPPY HEARTED", "HAPPYHEARTED", "HAR", "HARBINGER", "HARMONY"]


# O(n) for search. Naive algorithm
def complete_me(prefix: str, word_list: str):
    res = []

    for w in word_list:
        if w.startswith(prefix):
            res.append(w)

    return res


if __name__ == "__main__":
    assert complete_me("AD", words) == ["ADOXOGRAPHY", "ADUMBRATE"]
    assert complete_me("BE", words) == [
        "BE EXTRAORDINARY", "BE HAPPY", "BEATHA", "BEATIFY"]
