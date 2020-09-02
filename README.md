#team-management
Team management APIs for listing, creating, updating and deleting team records.

<h3>Setup:</h3>

1. Checkout the repository. Make sure docker compose is installed in your system.

2. Run below command inside parent repository folder.
<code>
  sudo docker-compose build
</code>

3. Bring up localhost server 
<code>
  sudo docker-compose up -d
</code>


 4. Run migrations
 <code>
  docker-compose run web python manage.py migrate
</code>


 5. Check localhost is accessible at 
<code>
   http://localhost:8000/admin
</code>
   It should show a login window. This shows that project is ready to use APIs.
   
   
 <h3>Usage:</h3>
 
 <h4>API Doc: </h4>
      API doc can be accessed at 
<code>
  http://localhost:8000/redoc/
</code>
  
  It gives an overview of available APIs and success response.
 
 <h4>List API - </h4>
<code>
curl --location --request GET 'http://localhost:8000/api/v1/teams/'
</code>

<h4>Create API - </h4>
<code>
curl --location --request POST 'http://localhost:8000/api/v1/teams/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "Neeraj",
    "last_name": "Sinha",
    "phone_number": "+919393939393",
    "email": "abc@gmail.com",
    "role": "admin"
}'
</code>

<h4> Get specific employee using id - </h4>

<code>
curl --location --request GET 'http://localhost:8000/api/v1/teams/1/'
</code>

<h4>Update any field of a team member for given id - </h4>

<code>
curl --location --request PATCH 'http://localhost:8000/api/v1/teams/1/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "xyz@gmail.com",
    "role": "regular"
}'
</code>
  
<h4>Delete a given team member record using its id - </h4>

<code>
curl --location --request DELETE 'http://localhost:8000/api/v1/teams/1/' \
--header 'Content-Type: application/json'
</code>

<h4>List team members by searching, filtering, sorting or using page number - </h4>

Currently by default 10 records are displayed in a single page.

Filtering based on first name - 

<code>
curl --location --request GET 'http://localhost:8000/api/v1/teams/?first_name=Neeraj' \
--header 'Content-Type: application/json'
</code>

Sorting based on last name - 

<code>
curl --location --request GET 'http://localhost:8000/api/v1/teams/?ordering=last_name' \
--header 'Content-Type: application/json'
</code>

Search all fields - 

<code>
curl --location --request GET 'http://localhost:8000/api/v1/teams/?search=9393' \
--header 'Content-Type: application/json'
</code>




