def get_full_name(first_name: str, last_name: str):
	full_name = first_name.title() + " " + last_name.title()
	return full_name


f = input("Enter your first name: ")
l = input("Enter your last name: ")

print(get_full_name(f, l))
