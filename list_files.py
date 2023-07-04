import os
import tkinter as tk
from tkinter import ttk, filedialog


def list_files_with_keywords(directory):
    files = []
    keywords = ["controller", "service", "dao", "proxy", "repository", "queries"]

    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if not (filename.endswith(".class") or filename.endswith(".bak")):
                folder_name = root.lower().split(os.path.sep)[-1]
                if any(keyword in folder_name for keyword in keywords):
                    files.append(os.path.join(root, filename))
    return files

def filter_files(search_query, search_file_names=True, search_folder_names=True):
    filtered_files = []
    for file_path in all_files:
        file_name = os.path.basename(file_path)
        folder_name = os.path.dirname(file_path)

        if search_file_names and search_query.lower() in file_name.lower():
            filtered_files.append(file_path)
        elif search_folder_names and search_query.lower() in folder_name.lower():
            filtered_files.append(file_path)
    return filtered_files

def generate_fe_service_code(method_name, return_type, parameter_names, parameter_types):
    # Create the parameter string
    parameters = ", ".join([f"{param_type} {param_name}" for param_name, param_type in zip(parameter_names, parameter_types)])

    code = f"""
// Frontend (FE) service code
public ResponseEntity<{return_type}> {method_name}({parameters});
"""
    return code

def generate_fe_implementation_code(method_name, return_type, parameter_names, parameter_types):
    # Create the parameter string
    parameters = ", ".join([f"{param_type} {param_name}" for param_name, param_type in zip(parameter_names, parameter_types)])

    code = f"""
// Frontend (FE) service implementation code
@Override
public ResponseEntity<{return_type}> {method_name}({parameters}) {{
    // TODO Auto-generated method stub
    return suretyCoverUwBEServiceClient.{method_name}();
}}
"""
    return code

def generate_feign_client_code(method_name, return_type, parameter_names, parameter_types):
    # Create the parameter string
    parameters = ", ".join([f"{param_type} {param_name}" for param_name, param_type in zip(parameter_names, parameter_types)])

    code = f"""
// Feign client code
@GetMapping(value = "/erp-peb-bank-uw-be/pebbank/surety-cover/uw/proposal/list")
public ResponseEntity<{return_type}> {method_name}({parameters}) ;
"""
    return code

def generate_be_controller_code(method_name, return_type, parameter_names, parameter_types):
    # Create the parameter string
    parameters = ", ".join([f"{param_type} {param_name}" for param_name, param_type in zip(parameter_names, parameter_types)])

    code = f"""
// Backend (BE) controller code
/**
 * Method to fetch all surety cover uw proposal records
 */
@GetMapping(value = "/proposal/list")
@ApiOperation(value = "Get list of surety cover proposal records")
public ResponseEntity<{return_type}> {method_name}({parameters}) {{
    return ResponseEntity.ok(suretyCoverUwService.{method_name}());
}}
"""
    return code


def generate_be_service_code(method_name, return_type, parameter_names, parameter_types):
    # Create the parameter string
    parameters = ", ".join([f"{param_type} {param_name}" for param_name, param_type in zip(parameter_names, parameter_types)])

    code = f"""
public {return_type} {method_name}({parameters});
"""
    return code

def generate_be_service_impl_code(method_name, return_type, parameter_names, parameter_types):
    # Create the parameter string
    parameters = ", ".join([f"{param_type} {param_name}" for param_name, param_type in zip(parameter_names, parameter_types)])

    code = f"""

    @Override
    public {return_type} {method_name}({parameters}) {{
        return suretyCoverUwRepository.{method_name}();
    }}

"""
    return code

def generate_be_dao_code(method_name, return_type, parameter_names, parameter_types):
    # Create the parameter string
    parameters = ", ".join([f"{param_type} {param_name}" for param_name, param_type in zip(parameter_names, parameter_types)])

    code = f"""
public {return_type} {method_name}({parameters});
"""
    return code

def generate_be_dao_impl_code(method_name, return_type, parameter_names, parameter_types):
    # Create the parameter string
    parameters = ", ".join([f"{param_type} {param_name}" for param_name, param_type in zip(parameter_names, parameter_types)])

    code = f"""

    @Override
    public List<{return_type}> {method_name}({parameters}) {{
        // TODO: Implement DAO logic here
        return null;
    }}

"""
    return code


# def generate_fe_service_code(method_name, return_type, parameter_names, parameter_types):
#     # Create the parameter string
#     parameters = ", ".join([f"{param_type} {param_name}" for param_name, param_type in zip(parameter_names, parameter_types)])
#
#     code = f"""
# public ResponseEntity<{return_type}> {method_name}({parameters}) {{
#     // TODO: Add your code here
# }}
# """
#     return code

# def generate_be_controller_code(method_name, return_type, parameter_names, parameter_types):
#     # Create the parameter string
#     parameters = ", ".join([f"{param_type} {param_name}" for param_name, param_type in zip(parameter_names, parameter_types)])
#
#     code = f"""
# SuretyCoverUwController is controller in be
# /**
#  * Method to fetch all surety cover uw proposal records
#  */
# @GetMapping(value = "/proposal/list")
# @ApiOperation(value = "Get list of surety cover proposal records")
# public ResponseEntity<{return_type}> {method_name}({parameters}) {{
#     // TODO: Add your code here
# }}
# """
#     return code

def generate_code():
    method_name = method_name_entry.get()
    return_type = return_type_entry.get()
    parameter_names = parameter_names_entry.get().split(",")  # Get parameter names as a list
    parameter_types = parameter_types_entry.get().split(",")  # Get parameter types as a list

    if not method_name:
        print("Please enter a method name.")
        return
    if not return_type:
        print("Please enter a return type.")
        return
    if len(parameter_names) != len(parameter_types):
        print("Parameter names and types must have the same number of elements.")
        return

    selected_files = [listbox.get(index) for index in listbox.curselection()]
    print("Selected Files:")
    for file_path in selected_files:
        print(file_path)
        # Read the contents of the file
        with open(file_path, 'r') as file:
            file_contents = file.readlines()
        # Find the last line containing a closing curly brace
        last_line_index = None
        for i in range(len(file_contents) - 1, -1, -1):
            if '}' in file_contents[i]:
                last_line_index = i
                break
        if last_line_index is None:
            print("No closing curly brace found in the file.")
            continue
        # Check if the file contains the keyword
        with open(file_path, 'r') as file:
            file_contents = file.read()

        if "service" in file_path.lower() and ("fe" in file_path.lower()):

            # Insert the generated code at the appropriate position
            fe_service_code = generate_fe_service_code(method_name, return_type, parameter_names, parameter_types)

            file_contents = file_contents.splitlines()
            file_contents.insert(last_line_index, fe_service_code)
            file_contents = '\n'.join(file_contents)
            with open(file_path, 'w') as file:
                file.write(file_contents)

        elif "serviceimpl" in file_path.lower() and ("fe" in file_path.lower()):
            # Insert the generated code at the appropriate position
            fe_service_impl_code = generate_fe_implementation_code(method_name, return_type, parameter_names, parameter_types)

            file_contents = file_contents.splitlines()
            file_contents.insert(last_line_index, fe_service_impl_code)
            file_contents = '\n'.join(file_contents)

            # Write the modified contents back to the file
            with open(file_path, 'w') as file:
                file.write(file_contents)

        elif "client" in file_path.lower():
            # Insert the generated code at the appropriate position
            be_client_code = generate_feign_client_code(method_name, return_type, parameter_names, parameter_types)

            file_contents = file_contents.splitlines()
            file_contents.insert(last_line_index, be_client_code)
            file_contents = '\n'.join(file_contents)

            # Write the modified contents back to the file
            with open(file_path, 'w') as file:
                file.write(file_contents)
        elif "controller" in file_path.lower():
            # Insert the generated code at the appropriate position
            be_controller_code = generate_be_controller_code(method_name, return_type, parameter_names, parameter_types)

            file_contents = file_contents.splitlines()
            file_contents.insert(last_line_index, be_controller_code)
            file_contents = '\n'.join(file_contents)

            # Write the modified contents back to the file
            with open(file_path, 'w') as file:
                file.write(file_contents)

        elif "service" in file_path.lower() and ("be" in file_path.lower()):
            # Insert the generated code at the appropriate position
            be_service_code = generate_be_service_code(method_name, return_type, parameter_names, parameter_types)

            file_contents = file_contents.splitlines()
            file_contents.insert(last_line_index, be_service_code)
            file_contents = '\n'.join(file_contents)

            # Write the modified contents back to the file
            with open(file_path, 'w') as file:
                file.write(file_contents)

        elif "serviceimpl" in file_path.lower() and ("be" in file_path.lower()):
            # Insert the generated code at the appropriate position
            be_service_impl_code = generate_be_service_impl_code(method_name, return_type, parameter_names, parameter_types)

            file_contents = file_contents.splitlines()
            file_contents.insert(last_line_index, be_service_impl_code)
            file_contents = '\n'.join(file_contents)

            # Write the modified contents back to the file
            with open(file_path, 'w') as file:
                file.write(file_contents)

        elif "dao" in file_path.lower():
            # Insert the generated code at the appropriate position
            be_dao_code = generate_be_dao_code(method_name, return_type, parameter_names, parameter_types)

            file_contents = file_contents.splitlines()
            file_contents.insert(last_line_index, be_dao_code)
            file_contents = '\n'.join(file_contents)

            # Write the modified contents back to the file
            with open(file_path, 'w') as file:
                file.write(file_contents)

        elif "daoimpl" in file_path.lower():
            # Insert the generated code at the appropriate position
            be_dao_impl_code = generate_be_dao_impl_code(method_name, return_type, parameter_names, parameter_types)

            file_contents = file_contents.splitlines()
            file_contents.insert(last_line_index, be_dao_impl_code)
            file_contents = '\n'.join(file_contents)

            # Write the modified contents back to the file
            with open(file_path, 'w') as file:
                file.write(file_contents)




def search_files(event=None):
    search_query = search_query_entry.get()
    search_file_names = search_file_names_var.get() == 1
    search_folder_names = search_folder_names_var.get() == 1

    filtered_files = filter_files(search_query, search_file_names, search_folder_names)

    # Get the selected files before updating the listbox
    selected_files = [listbox.get(index) for index in listbox.curselection()]

    listbox.delete(0, tk.END)  # Clear existing items
    for file in filtered_files:
        listbox.insert(tk.END, file)

    # Reselect the previously selected files
    for file in selected_files:
        try:
            index = filtered_files.index(file)
            listbox.select_set(index)
        except ValueError:
            pass

# Create the GUI window
root = tk.Tk()
root.title("File Selection")
root.geometry("700x400")

# Create search options
search_frame = tk.Frame(root, padx=10, pady=10)
search_frame.pack()

search_label = tk.Label(search_frame, text="Search:", font=("Helvetica", 12))
search_label.pack(side=tk.LEFT)

search_query_entry = tk.Entry(search_frame, font=("Helvetica", 12))
search_query_entry.pack(side=tk.LEFT, padx=5)
search_query_entry.bind("<KeyRelease>", search_files)  # Bind the search functionality to KeyRelease event

search_file_names_var = tk.IntVar()
search_folder_names_var = tk.IntVar()

search_file_names_cb = tk.Checkbutton(search_frame, text="Search File Names", variable=search_file_names_var, font=("Helvetica", 10), command=search_files)
search_folder_names_cb = tk.Checkbutton(search_frame, text="Search Folder Names", variable=search_folder_names_var, font=("Helvetica", 10), command=search_files)

search_file_names_cb.select()  # Default: Search file names
search_folder_names_cb.select()  # Default: Search folder names

search_file_names_cb.pack(side=tk.LEFT, padx=5)
search_folder_names_cb.pack(side=tk.LEFT)

# Create input fields for method name, return type, parameter names, and parameter types
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack()

method_name_label = tk.Label(input_frame, text="Method Name:", font=("Helvetica", 12))
method_name_label.grid(row=0, column=0, sticky=tk.W)

method_name_entry = tk.Entry(input_frame, font=("Helvetica", 12))
method_name_entry.grid(row=0, column=1, padx=5)

return_type_label = tk.Label(input_frame, text="Return Type:", font=("Helvetica", 12))
return_type_label.grid(row=0, column=2, sticky=tk.W)

return_type_entry = tk.Entry(input_frame, font=("Helvetica", 12))
return_type_entry.grid(row=0, column=3, padx=5)

parameter_names_label = tk.Label(input_frame, text="Parameter Names:", font=("Helvetica", 12))
parameter_names_label.grid(row=1, column=0, sticky=tk.W)

parameter_names_entry = tk.Entry(input_frame, font=("Helvetica", 12))
parameter_names_entry.grid(row=1, column=1, padx=5)

parameter_types_label = tk.Label(input_frame, text="Parameter Types:", font=("Helvetica", 12))
parameter_types_label.grid(row=1, column=2, sticky=tk.W)

parameter_types_entry = tk.Entry(input_frame, font=("Helvetica", 12))
parameter_types_entry.grid(row=1, column=3, padx=5)

listbox_frame = tk.Frame(root, padx=10, pady=10)
listbox_frame.pack(fill=tk.BOTH, expand=True)

listbox_scrollbar = ttk.Scrollbar(listbox_frame)
listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(listbox_frame, selectmode=tk.MULTIPLE, font=("Helvetica", 11))
listbox.pack(fill=tk.BOTH, expand=True)

listbox.config(yscrollcommand=listbox_scrollbar.set)
listbox_scrollbar.config(command=listbox.yview)

# Populate the listbox initially
project1_path = "D:/codesinwardoutward/erp_io_io_fe1"
project2_path = "D:/codesinwardoutward/erp_io_io_be"

all_files = list_files_with_keywords(project1_path) + list_files_with_keywords(project2_path)
search_files()

# Create a button to generate code
generate_button = ttk.Button(root, text="Generate Code", command=generate_code)
generate_button.pack(pady=10)

# Set custom colors
root.configure(background='#F0F0F0')
search_frame.configure(background='#F0F0F0')
input_frame.configure(background='#F0F0F0')
listbox_frame.configure(background='#F0F0F0')
search_label.configure(background='#F0F0F0')
method_name_label.configure(background='#F0F0F0')
return_type_label.configure(background='#F0F0F0')
parameter_names_label.configure(background='#F0F0F0')
parameter_types_label.configure(background='#F0F0F0')

# Start the GUI event loop
root.mainloop()
