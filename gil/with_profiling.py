import contextlib
import threading


def profile_function(frame, event, arg):
    print(f"Thread {threading.current_thread().name} :: {event=} {arg=} {frame=} ")
    return profile_function


@contextlib.contextmanager
def with_profiling():
    # Set a profile function
    threading.setprofile(profile_function)
    yield
    # Remove the profile function when done
    threading.setprofile(None)
