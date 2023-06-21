#!/usr/bin/env python
# coding: utf-8

# #         Assignment 01 Solutions

# ### 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# 
#  "`*`,`'hello'`, `-87.8`,`-`,`/`,`+`,`6`"
#  

# **Ans:**
# 
# **Values are -** `'hello' `, `-87.8 `, `6`
# 
# **Expressions are -** `*` ,`-` ,` /` , `+`

# ### 2. What is the difference between string and variable?

# **Ans:** 
# A String is the information stored in a variable. It is usually a group of characters or a single character in double quotes `""` or single quotes `''`.
# 
# While a Variable is used to store informations

# ### 3. Describe three different data types.

# **Ans:** These are three different data types :
# 
# `str` - A String is an ordered sequence of characters.
# 
# `int` - An Integer is used to represent whole numbers.
# 
# `float` - A Float is used to represent decimal number.

# In[5]:


# Example for Str :
string  = "hello"
print(string, type(string))
# Example for int :
integer = 123
print(integer,type(integer))
# Example for float :
floaat = 33.33
print(floaat,type(floaat))


# ### 4. What is an expression made up of? What do all expressions do?

# **Ans:** An expression is a combination of values, variables, operators, and calls to functions. Expressions need to be evaluated. If we ask Python to print an expression, the interpreter evaluates the expression and displays the result.

# In[13]:


# Example of expression :
2*2+4-8  #This is an expression

# After interpreter evalutes the expression, the result will be displayed for this expression as "0"


# ### 5.This assignment statements, like spam = 10. What is the difference between an expression and a statement?

# **Ans:** An expression is a combination of values, variables, and operators.When we type an expression at the prompt, the interpreter evaluates it, which means that it finds the value of the expression.
# 
# While a statement is a unit of code that has an effect, like creating a variable or displaying a value.When we type a statement, the interpreter executes it, which means that it does whatever the statement says. In general, statements don’t have values.

# In[14]:


# Example :
2*2+4-8  #This is an expression
var_name = "Hello World!" #This is an statement
print("Hello World!") #This is an expression statement


# ### 6. After running the following code, what does the variable bacon contain?
# `bacon = 22`
# 
# `bacon + 1`

# **Ans:** The variable `bacon` will contain the value `22`. Following are the example of the code.

# In[16]:


# Example 1 

bacon = 22
bacon + 1
print(bacon)


# In[18]:


# Example 2
# To change the bacon value correxct code is:

bacon = 22
bacon = bacon + 1
print(bacon)


# ### 7.What should the values of the following two terms be?
# `'spam'+'spamspam'`
# 
# `'spam'*3`

# **Ans:** Both expressions evaluate to the string `'spamspamspam'` Where as the first expression follows `String Concatentation` and the second expression follows `String Multiplication`

# In[20]:


# Example
'spam'+'spamspam' #this is a string concatentation
'spam'*3  #this is string multiplication


# ### 8. Why is eggs a valid variable name while 100 is invalid?

# **Ans:** As per Python rules for the variables, numbers are not allowed as the variable names as `100` is a number, it is not allowed as variable name.
# 
# While `eggs` is a word made up with letters, hence it is allowed as variable name.

# In[23]:


# For Example
eggs = 'Hello'   #Variable in letter
100 = 'World!'   #Variable in Number

print(eggs)   #Prints the value of eggs i.e. 'Hello'
print(100)    #Throws a SyntaxError mentioned below


# ### 9. What three functions can be used to get the integer, floating-point number, or string version of a value?

#  **Ans:** The `int()`,`float()`,and `str()` functions will evaluate to the integer,floating-point number,string version of the value passed to them.

# In[25]:


#Example :

print('int(10.0) -> ',int(3.5))  # int() function converts given input to int
print('float(10) -> ',float(35))  # float() function converts given input to float
print('str(10) -> ',str(10))      # str() function converts given input to string


# ### 10.Why does this expression cause an error? how can you fix it? 
# `'I have eaten ' + 99 + 'burritos.'`

# **Ans:** This cause of error is 99. Because 99 is not a string. 99 must be typecasted to a string to fix this error. the correct way is:

# In[39]:


#Example 1
'I have eaten ' + "99" + ' burritos.'    #Typecast 99 as a string in quotes
            #or
'I have eaten ' + str(99) + ' burritos.'  #Typecast 99 as a string in str() format

