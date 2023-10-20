def compute_checksum(data_list):
    """
    Calculate the Internet Checksum for the provided data list.
    Input: list of 16-bit data (usually in hexadecimal).
    Output: Checksum in hexadecimal.
    """

    # Sum all the 16-bit words using 32-bits for intermediate calculations.
    total_sum = sum([int(word, 16) for word in data_list]) & 0xFFFFFFFF

    # Add carries until no more carry is left.
    while total_sum >> 16:
        total_sum = (total_sum & 0xFFFF) + (total_sum >> 16)

    # Take the one's complement.
    checksum = ~total_sum & 0xFFFF

    return format(checksum, '04X')


def check_received_data(data_list):
    """
    Check the received data's checksum.
    Input: list of 16-bit data including checksum (usually in hexadecimal).
    Output: True if no error, False otherwise.
    """

    # Check if the calculated checksum with received data results in FFFF.
    return compute_checksum(data_list) == "FFFF"


# Test with the provided example:
data = ["0100", "F203", "F4F5", "F6F7"]
checksum = compute_checksum(data)
print(f"Checksum: {checksum}")  # Should print 210E

received_data = ["0100", "F203", "F4F5", "F6F7", "210E"]
print(check_received_data(received_data))  # Should print True
