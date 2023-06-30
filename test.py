import javalang

def analyze_java_file(file_path):
    with open(file_path, 'r') as file:
        java_source_code = file.read()

    # Parse the Java source code
    try:
        tree = javalang.parse.parse(java_source_code)
    except javalang.parser.JavaSyntaxError as e:
        return [f"Syntax error in {file_path}: {e.description}"]

    # Perform error detection checks
    errors = []
    # Example error detection: Check for unused private fields
    for _, field in tree.filter(javalang.tree.FieldDeclaration):
        modifiers = [modifier.name for modifier in field.modifiers]
        if 'private' in modifiers:
            field_name = field.declarators[0].name
            used = any(field_name in expr.value for _, expr in tree.filter(javalang.tree.VariableDeclarator))
            if not used:
                errors.append(f"Unused private field: {field_name}")

    return errors

# Provide the path to your Java file
file_path = 'D:/codesinwardoutward/erp_io_io_fe1/src/main/java/in/ecgc/smile/erp/io/io/fe/service/InwardService.java'


# Analyze the Java file and retrieve errors
file_errors = analyze_java_file(file_path)

# Print the detected errors
if file_errors:
    print("Detected Errors:")
    for error in file_errors:
        print(error)
else:
    print("No errors detected.")
