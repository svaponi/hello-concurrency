import contextlib
import sys
import threading


def trace_function(frame, event, arg):
    if event != "line":
        print(f"Thread {threading.current_thread().name} :: {event=} {arg=} {frame=} ")
    return trace_function


@contextlib.contextmanager
def with_trace():
    # Set a profile function
    sys.settrace(trace_function)
    yield
    # Remove the profile function when done
    sys.settrace(None)
