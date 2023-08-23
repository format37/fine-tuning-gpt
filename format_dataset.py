import json

def extract_json_objects_from_spaces(content):
    objects = []
    buffer = ""
    inside_brackets = 0

    for char in content:
        buffer += char
        if char == '{':
            inside_brackets += 1
        elif char == '}':
            inside_brackets -= 1
            if inside_brackets == 0:
                objects.append(buffer.strip())
                buffer = ""

    return objects


def reformat_objects_including_assistant(objects):
    reformatted_objects = []

    for obj_str in objects:
        obj = json.loads(obj_str)
        messages = obj.get("messages", [])
        system_message = next((msg for msg in messages if msg['role'] == 'system'), None)
        user_message = next((msg for msg in messages if msg['role'] == 'user'), None)
        assistant_message = next((msg for msg in messages if msg['role'] == 'assistant'), None)

        if system_message and user_message and assistant_message:
            reformatted_line = json.dumps({"messages": [system_message, user_message, assistant_message]}, ensure_ascii=False)
            reformatted_objects.append(reformatted_line)

    return reformatted_objects



def transform_file(input_path, output_path):
    with open(input_path, 'r') as file:
        content = file.read()
        content_with_spaces = content.replace("\n", " ")
        json_objects_from_spaces = extract_json_objects_from_spaces(content_with_spaces)
        reformatted_lines_from_spaces = reformat_objects_including_assistant(json_objects_from_spaces)

    with open(output_path, 'w') as file:
        file.write("\n".join(reformatted_lines_from_spaces))

# Example usage
input_path = 'dataset_multi.txt'
output_path = 'dataset.jsonl'
transform_file(input_path, output_path)
