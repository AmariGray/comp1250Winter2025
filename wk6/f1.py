"""
function: a variable/name
    that organising multiple steps

cook
    cook is an action
    
    get ingredients: values
    heat ingredients: actions/calculations
    serve final product: printing or outputting product

store all the steps to cook and then 
be able to CALL these steps at any given time

diff b/t loop and function
    loop runs statements at that specific time 
    of execution for that specific amount of times
    
    function: runs statements at that specific times
        of execution. YOU decide the amount of times.
        REPEAT by recalling function

benefit of function: you can vary the bahaviour
    cook
        cook what?
        cook at what time?
        cook with what cooking material 

adding parameters to function => alters/varies the 
behaviour of the function

argument: value that you pass to the function when 
USING/CALLING the function

parameter: a declared variable that allows user 
to vary the bahaviour of the function 

"""
# declare a function
def cook(what:str, at_what_time:int):  # adding parameters
    # params are local variables inside of function
    if isinstance(what, str) and isinstance(at_what_time, int):
        return f"You are cooking {what} at {at_what_time}"
    else:
        return "Error!"
# call a function
#value = cook()  # ()  => execute/run
value = cook("pasta", "10pm")  # arguments
print(value)
value = cook("pizza", "12pm")
print(value)
value = cook(at_what_time=8, what='eggs')
print(value)
