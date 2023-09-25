# Stage 3 

after implementing our simple models and create our relations between tables  don't Worry jounguini will make the Data-types stage but for now we want to focus how we Can make Quires using orm how we can Create read update or delete .
how we will query the database right now !!
i hate sql quires that looks like 
```
    SELECT * from tableName ; 

```
no need for this nowadays and now we all know that because of the ORM  و 
we are we are now only dealing with our classes as the Object way 
as once you inherited from 'models.Model' there is alot of hidden work has been done 
but one of the most important thing has the inhertance the ManagerClass  that is responible for 
managing quiries the Class called objects so According to our Database we have 
	Company , Programmer , Languages 
so for each class we can access the objects using :
try  python manage.py shell : 
```	
    from Base.models import Company
    Company.objects
```
that will say that objects is the ManagerClass that allows you to manage Queries on your model 
    Create , Read , Update , Delete

## Lets Create and Update a record  in the Company  ?
    to Create a record inside your migrated models becuase of the ORM you don't have to worry about SQL 
    all what you will care is the OBJECT and how to deal with 
    so for Example we have Company class if we want to Create instance we will say 
    ```
        from base.models import Company 

        apple = Company(name='Apple')
    ```   
    with this you have created instance of the Company named Apple as the name is only the  instance member ,
    dont forget that we inhertied from models.Model so there is alot behind the seen so apple now is a magical instance 
    all what you need to save the instance to the Database is assign the save() method
    to be like this :
    ```
        from base.models import Company 

        apple = Company(name='Apple')
        apple.save() #now saved to the Database 
    ```   
    also if you alter the instance name and save it will update 

    ```
        from base.models import Company 

        apple = Company(name='Apple')
        apple.save()
        apple.name = "Microsoft" #update instance info 
        apple.save() #saving the data updated 

    ```   

### 2. Let's Delete a company :  

supposing that you still has the Instance all what you will need to do is calling the .delete() method

```
    apple.delete()
```


## 3. Slecting and Filtering Data :

Selecting and Filtering the Data is one of the most repitive tasks that you will do each Project
so let's take about selecting First and the options then i will leave you with a prepared sheet for the Filtering 

in selecting we will deal with selecting or getting all elements in the table and to get only sepecific one element 

### selecting all Element :  
```
    from base.models import Company 
    query = Company.objects.all() 
    #this will retrieve list of objects inside the table created 
    #orm make it easy for you 

```
### Selecting specific element with condition :

get() method allows you to pass argument to get only specific element upon certain information
like this 
```
    from base.models import Company 
    apple = Company.objects.get(id=1) 
    
    #retrieve the object directly not a list
    #it could be with name but its not unique so it will return 
    
    #first match 
    apple = Company.objects.get(name='Apple') 

```


once selecting you can perform operations on it but what about Filtering our data 


# Data Filtering 

this list provided bellow is all about how to get quires with condition or exclude data from the Query 
its full with lookups with is our data Filtering proccess and also about how we can chain our quires 

```
    Language.object.filter(col__filter='value)

	Language.object.filter(col__exact='value)
	
	Language.object.filter(col__iexact='value) #non case senstive

	Language.object.filter(col__iexact='value).filter(name__exact='python') #chaining filter

	Language.object.exclude(col__iexact='value) # all except the value 

	Language.object.filter(col__gte='value) #greater than value 
	
q	Language.object.filter(col__lt='value) #less than 

	Language.object.filter(col__contains='value) # copntains sub part of the value 

	Language.object.filter(col__icontains='value) #non case senstive 

	Language.object.filter(name__in=['usif','adel','ahmed' ]) #will return them if found
	
	 Language.object.exclude(name__in=['usif','adel','ahmed' ]) #all except the values 

	 Language.object.filter(name__istartswith='us') #all that match the same start value  

	Language.object.filter(name__iendswith='f') #all that match the same end value  
	
	Language.object.filter(age__isnull=True) #all the null age
 
	Programmer.objects.count() #return programmers Count 
	
	Language.object.filter(name__iendswith='f').count() #chainig the quiries 

```

# Contributing
If you'd like to contribute to this project, please follow these guidelines for code contributions, bug reporting, and feature requests.

# License
This project is licensed under the MIT License.  

# Acknowledgments
Give credit to any individuals, projects, or libraries that inspired or helped you with this project.

