import ipaddress

class ConsoleApp:
    def __init__(self):
        self.system_facts = {}

    def main(self):
        while True:
            try:
                # Display a simple command prompt
                user_input = input("Enter command (or 'exit' to quit): ")
                user_input = user_input.lower()

                # Exit condition
                if user_input == 'q' or user_input == 'exit' or user_input == 'quit':
                    break

                # Handle different commands
                if user_input == 'mac':
                    self.system_facts = self.create_db("rack2-pxe-mac.txt")
                elif user_input == 'ip':
                    self.create_ip()
                else:
                    print("Unknown command.")

            except Exception as e:
                print(f"An error occurred: {e}")

    def create_db(self, filename):
        facts_dict = {}
        text_file = open(filename, 'r')

        facts_dict["macaddr"] = text_file.read().split('\n')
        return facts_dict

    def create_ip(self):
        qty = len(self.system_facts["macaddr"])
        while True:
            ip_cidr = input("Enter the IP CIDR: ")

            if self.validate_ip(ip_cidr) == False:
                break

#        for i in range(qty):

    def validate_ip(self, cidr):
        try:
            if cidr is not None:
                ipaddress.ip_network(cidr)
                print(f"Valid CIDR: {cidr}")
                return False
            else:
                print("No IP provided!")
        except ValueError:
            print("Invalid CIDR format")


if __name__ == "__main__":
    app = ConsoleApp()
    app.main()
