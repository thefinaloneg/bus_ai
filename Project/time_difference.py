import time
import arrive
import csv_handler
import time_handler
import stop_id_retriever


# Outcome of whether current several buses came before or after the scheduled or expected time -> 3 for scheduled,
# 4 or expected

def bulk_difference(stop_id):
    sc_ex = 4
    results = []
    bus_headsign = arrive.arrival_queue(stop_id)
    if bus_headsign is False:
        print(stop_id + " does not exist.")
        return
    csv_handler.start_csv()
    for i in range(0, 20):  # change depending on how many departures want to be monitored, will run consecutively as
        # a queue for each departure
        bus_headsign = arrive.arrival_queue(stop_id)
        if bus_headsign != []:  # if the arrival queue is NOT empty
            try:
                original_expected = stop_id_retriever.stop_id_info(stop_id)[bus_headsign[0]][4]
                current_routeid = stop_id_retriever.stop_id_info(stop_id)[bus_headsign[0]][0]
            except (KeyError, TypeError) as e:
                break
            while True:
                if arrive.arrival_queue(stop_id)[1] == bus_headsign[0]:  # if the values are swapped if block
                    break
                elif arrive.arrival_queue(stop_id)[0] != bus_headsign[0]:
                    if len(results) != 0:  # accounts for buses that arrive before the range, improbable but did happen
                        csv_handler.append_csv(stop_id, bus_headsign[0], current_routeid,
                                               time_handler.time_converter(original_expected, "soft"),
                                               str(results[len(results) - 1]))
                        print('Arrived at: ' + str(results[len(results) - 1]))
                        break
                    else:  # eliminate this whole block later, was made for this particular print
                        print('Arrived at: ' + int(
                            time_handler.time_difference(stop_id, bus_headsign[0], sc_ex, original_expected)))
                        csv_handler.append_csv(stop_id, bus_headsign[0], current_routeid,
                                               time_handler.time_converter(original_expected, "soft"),
                                               str(results[len(results) - 1]))
                        break
                if -120 <= int(
                        time_handler.time_difference(stop_id, bus_headsign[0], sc_ex, original_expected)) <= 300:
                    print("Current time difference: " + str(
                        time_handler.time_difference(stop_id, bus_headsign[0], sc_ex, original_expected)))
                    print("Expected time: " + original_expected + "\n")
                    results.append(
                        int(time_handler.time_difference(stop_id, bus_headsign[0], sc_ex, original_expected)))
                    time.sleep(3)
                else:
                    print("Time until next bus arrives: " + str(
                        time_handler.time_difference(stop_id, bus_headsign[0], sc_ex, original_expected)))
                    print("Expected time: " + original_expected + "\n")
                    results.append(
                        int(time_handler.time_difference(stop_id, bus_headsign[0], sc_ex, original_expected)))
                    time.sleep(30)
        else:  # if the arrival queue is empty
            print('No expected departures for the moment.')
            time.sleep(240)
