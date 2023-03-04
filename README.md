Author: Aaron Teel

Contact Info: ateel@uoregon.edu

Project Details: - This project is a web-based recreation of the ACP calculator used by RUSA, making use of MongoDB as a tool to store data values. The website, taking in the total race distance via a drop-down menu, taking in the start date via a date selector table, and taking the distances to the mid-race controls via a textbox with user input, will calculate the open and close times for each control that is passed into the grid, as well converting kilometers to miles and vice versa. The open times and close times will be displayed in the datetime format MM:DD HH:mm. There are also two buttons, 'Submit' and 'Display', which are the MongoDB functions. '

                - HOW TO USE: 
                    
                    - Step 1: Build your docker image with the command "docker build -t <insert image name here> ."

                    - Step 2: Run your docker image with the command "docker run -p 5001:5000 <image name>"

                    - Step 3: Open up a browser of your choosing and type into the search bar "http://localhost:5001" to boot up the web page

                    - Step 4: Select a total race distance using the left-hand drop-down menu and select a start time using the right hand table

                    - Step 5: Type in control distance values into the text boxes below "KM" or "Miles", then either press ENTER or click into another text box to display the open and close times for that control distance
    
                    - Step 6: Click the 'Submit' button in the top right-hand corner of the screen to add the controls to the MongoDB database

                    - Step 7: Click the 'Display' button to see the values you put into the database 

                - The open times and close times are calculated with the RUSA algorithm. This algorithm is as follows:

                    - For calculating the open times:

                        - Step 1: Take in a control distance, total race (brevet) distance, and start time

                        - Step 2: Calculate the hours and minutes that we need to shift by

                            - Step 2a: For any control between 0 and 200 km, divide the control distance by the maximum speed as regulated by RUSA, which in this case is 34 km/hr. Take the whole number from this division and round it down to get the number of hours, then take the remainder and multiply it by 60 to get the number of minutes 

                            - Step 2b: For any control between 200 and 400 km, we must first calculate the time for the first 200 km with a speed of 34 km/hr, then add the time for the remaining distance to the control at a speed of 32 km/hr 

                            - Step 2c: For any control between 400 and 600 km, we must first calculate the time for the first 400 km,  then add the time for remaining distance to the control at a speed of 30 km/hr 

                            - Step 2d: For any control between 600 and 1000 km, we must first calculate the time for the first 600 km, then add the time for the remaining distance to the control at a speed of 28 km/hr 

                        - Step 3: Once we have our hours and minutes, we must shift accordingly from our start time 

                    - For calculating the closing times:

                        - Step 1: Take in a control distance, total race (brevet) distance, and a start time

                        - Step 2: 

                            - Step 2a: For any control under 60 km, we must divide the control distance by 20, then add 1 to get an extra hour, since we don't want the control to close before the start closes

                            - Step 2b: For any control bewteen 60 and 600 km, we must divide the control distance by the minimum speed set by RUSA, which is 15 km/hr. We must then round down the whole number from this division to get the hours, then multiply the remainder by 60 to get the number of minutes

                            - Step 2c: For any control between 600 and 1000 km, we must first calculate the time for the first 600 km with a speed of 15 km/hr, then add the time for the remaining distance to the control at a speed of 11.428 km/hr

                        - Step 3: Once we have our hours and minutes, we must shift accordingly from our start time
