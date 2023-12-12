rules = {}
rule_name = None
keywords = ["input", "output", "script", "run", "shell", "notebook", "cwl", "params", "log", "wildcard_constraints", "benchmark", "threads", "resources", "message", "priority"]

with open("Snakefile", "r") as fin:
    for line in fin.readlines():
        line = line.strip()
        if line:
            if line.startswith("rule "):
                rule_name = line[5:-1].strip()
                rules[rule_name] = {}
            elif rule_name:
                for keyword in keywords:
                    if line.startswith(keyword + " "):
                        content = line[len(keyword):].strip()
                        rules[rule_name][keyword] = content
                        break

def ptxt(text):
    return '"' + text.replace("'", "").replace('"', '') + '"'

input2rule, rule2output = "", ""
data_node, rule_node = set(), set()
inputs, outputs = {}, {}

for rule_name, rule_content in rules.items():
    if "input" in rule_content:
        for input_item in rule_content["input"].split(","):
            input_item = input_item.strip()
            inputs[input_item] = rule_name
            data_node.add(input_item)
            input2rule += f"{ptxt(input_item)} -> {ptxt(rule_name)}\n"
    if "output" in rule_content:
        for output_item in rule_content["output"].split(","):
            output_item = output_item.strip()
            outputs[output_item] = rule_name
            data_node.add(output_item)
            rule2output += f"{ptxt(rule_name)} -> {ptxt(output_item)}\n"

flowchart = ""
for node in data_node:
    if node in inputs:
        flowchart += f"{ptxt(node)} -> {ptxt(inputs[node])}\n"
    if node in outputs:
        flowchart += f"{ptxt(outputs[node])} -> {ptxt(node)}\n"

print(flowchart)
