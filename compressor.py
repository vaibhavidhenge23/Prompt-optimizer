import re

def count_tokens(text):
    words = len(text.split())
    return round(words / 0.75)

FILLERS = [
    # Request phrases
    r"\bi would like to\b",
    r"\bi would love to\b",
    r"\bi want to\b",
    r"\bi need to\b",
    r"\bi was wondering if\b",
    r"\bi was hoping\b",
    r"\bcould you please\b",
    r"\bcould you kindly\b",
    r"\bcould you\b",
    r"\bwould you please\b",
    r"\bwould you kindly\b",
    r"\bwould you\b",
    r"\bcan you please\b",
    r"\bcan you\b",
    r"\bwill you\b",
    r"\bmight you\b",
    r"\bi need you to\b",
    r"\bi want you to\b",
    r"\bplease help me\b",
    r"\bhelp me\b",
    r"\bkindly\b",
    r"\bplease\b",

    # Filler adverbs
    r"\bbasically\b",
    r"\bactually\b",
    r"\bliterally\b",
    r"\bvirtually\b",
    r"\bessentially\b",
    r"\bfundamentally\b",
    r"\bgenerally\b",
    r"\btypically\b",
    r"\busually\b",
    r"\bnormally\b",
    r"\bsimply\b",
    r"\bjust\b",
    r"\bvery\b",
    r"\breally\b",
    r"\bquite\b",
    r"\brather\b",
    r"\bsomewhat\b",
    r"\bkind of\b",
    r"\bsort of\b",
    r"\ba bit\b",
    r"\ba little\b",
    r"\byou know\b",
    r"\bi mean\b",
    r"\blike\b",
    r"\bso\b",
    r"\bwell\b",
    r"\banyway\b",
    r"\banyways\b",
    r"\bobviously\b",
    r"\bclearly\b",
    r"\bcertainly\b",
    r"\bdefinitely\b",
    r"\babsolutely\b",
    r"\bof course\b",
    r"\bsurely\b",

    # Politeness
    r"\bthank you\b",
    r"\bthanks\b",
    r"\bmany thanks\b",
    r"\bif possible\b",
    r"\bif you don't mind\b",
    r"\bif you could\b",
    r"\bat your earliest convenience\b",
    r"\bas soon as possible\b",
    r"\basap\b",

    # Redundant starters
    r"\bplease note that\b",
    r"\bplease be aware that\b",
    r"\bi should mention that\b",
    r"\bi should note that\b",
    r"\bas i mentioned\b",
    r"\bas i said\b",
    r"\bas previously mentioned\b",
    r"\bto be honest\b",
    r"\bhonestly\b",
    r"\btruthfully\b",
    r"\bfrankly\b",
    r"\bto tell you the truth\b",
    r"\bto be fair\b",
    r"\bto be clear\b",
    r"\bjust to clarify\b",
    r"\bjust to be clear\b",
    r"\bfor what it's worth\b",
    r"\bfwiw\b",

    # Weak openers
    r"\bi think\b",
    r"\bi believe\b",
    r"\bi feel\b",
    r"\bi suppose\b",
    r"\bi guess\b",
    r"\bi assume\b",
    r"\bi reckon\b",
    r"\bin my opinion\b",
    r"\bin my view\b",
    r"\bimo\b",
    r"\bimho\b",
    r"\bperhaps\b",
    r"\bmaybe\b",
    r"\bpossibly\b",
    r"\bprobably\b",

    # Extra words
    r"\bknow\b",
    r"\bthat\b",
    r"\bwhich\b",
    r"\bwho\b",
    r"\bwhere\b",
    r"\bwhen\b",
]
REPLACEMENTS = {
    # Difference/comparison
    "what is the difference between": "difference:",
    "what are the differences between": "differences:",
    "compare": "vs",
    "comparison between": "vs",

    # How/explain
    "how does": "how",
    "how do": "how",
    "how can": "how",
    "how should": "how",
    "explain to me": "explain",
    "explain in detail": "explain",
    "give me an explanation of": "explain",
    "give me a brief explanation": "explain briefly",
    "give me an overview of": "overview:",
    "tell me about": "about:",
    "tell me how": "how",

    # Provide/give
    "provide me with": "give",
    "provide me": "give",
    "give me information about": "info:",
    "give me details about": "details:",
    "give me an example of": "example:",
    "give me examples of": "examples:",

    # Write/create
    "write me a": "write",
    "write me an": "write",
    "create me a": "create",
    "create me an": "create",
    "make me a": "make",
    "make me an": "make",
    "generate me a": "generate",
    "generate me an": "generate",
    "build me a": "build",

    # Summary
    "give me a summary of": "summarize:",
    "give me a brief summary": "summarize briefly:",
    "summarize for me": "summarize:",
    "can you summarize": "summarize:",

    # List
    "give me a list of": "list:",
    "list down": "list:",
    "list out": "list:",
    "what are the": "list:",
    "what is the": "what:",

    # Verbose phrases → short
    "in order to": "to",
    "due to the fact that": "because",
    "at this point in time": "now",
    "in the event that": "if",
    "in spite of the fact that": "although",
    "with regard to": "about",
    "with respect to": "about",
    "in relation to": "about",
    "as a result of": "because",
    "for the purpose of": "for",
    "in the near future": "soon",
    "at the present time": "now",
    "on a daily basis": "daily",
    "in a timely manner": "quickly",
    "a large number of": "many",
    "a majority of": "most",
    "a number of": "some",
    "the majority of": "most",

    # Redundant adjectives
    "comprehensive": "",
    "detailed": "",
    "thorough": "",
    "complete": "",
    "full": "",
    "entire": "",
    "overall": "",
    "general": "",
    "various": "",
    "different": "",
    "multiple": "",
    "numerous": "",
    "several": "",
    "certain": "",
}

def compress(text):
    result = text.lower().strip()
    for k, v in REPLACEMENTS.items():
        result = result.replace(k, v)
    for filler in FILLERS:
        result = re.sub(filler, "", result, flags=re.IGNORECASE)
    result = re.sub(r"\s+", " ", result).strip()
    result = re.sub(r"\s([?.!,])", r"\1", result)
    return result

def run(text):
    before = count_tokens(text)
    compressed = compress(text)
    after = count_tokens(compressed)
    saved = before - after
    pct = round((saved / before) * 100) if before > 0 else 0
    print(f"\nOriginal   ({before} tokens): {text}")
    print(f"Compressed ({after} tokens): {compressed}")
    print(f"Saved: {saved} tokens ({pct}%)")

# --- Tests ---
run("I would like to know that basically what is the actual difference between python and javascript programming languages")
run("Could you please kindly help me understand how does machine learning actually work in detail?")
run("I was wondering if you could provide me with a comprehensive explanation of neural networks please")