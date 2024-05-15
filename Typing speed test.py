from time import time

def tperror(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors += 1
        else:
            if inwords[i] == words[i]:
                continue
            else:
                errors += 1

    return errors
    
def speed(inprompt, stime, etime):
    global time
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    time = elapsedtime(stime, etime)
    speed = twords / (time / 60)  # Speed in words per minute

    return speed

def elapsedtime(stime, etime):
    time_elapsed = etime - stime
    return time_elapsed

prompt = "Code is poetry written in a language only computers understand. Programming is the art of telling a machine what to do beautifully."

print("Type this:- '", prompt, "'")

stime = time()
inprompt = input()
etime = time()

time_taken = round(elapsedtime(stime, etime), 2)
speed_value = speed(inprompt, stime, etime)
errors = tperror(prompt)

print("Total time elapsed: ", time_taken, "seconds")
print("Your Average Typing speed was ", speed_value, "words per minute (w/m)")
print("With a total of", errors, "errors")
