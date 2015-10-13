from room_states import rooms_states


def print_current_room(current_room):
    print("DEBUG_NOTICE: PRINT CURRENT ROOM " + current_room["name_ID"])


def print_current_room_state(current_room):
    print("DEBUG_NOTICE: PRINT CURRENT ROOM STATE " + str(rooms_states[current_room["name_ID"]]["state"]) + "\n")\



def print_line(text, text_2):
    print("DEBUG_NOTICE: " + str(text_2) + " " + str(text))
