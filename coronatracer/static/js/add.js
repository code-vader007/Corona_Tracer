document.addEventListener('DOMContentLoaded', () => {

      document.querySelector('#contact').onsubmit = () => {

          // Initialize new request
          const request = new XMLHttpRequest();
          const contact1 = document.querySelector('#contact1').value;
          const contact2 = document.querySelector('#contact2').value;
          request.open('POST', '/convert');

          // Callback function for when request completes
          request.onload = () => {

              // Extract JSON data from request
              const data = JSON.parse(request.responseText);

              // Update the result div
              if (data.success) {
                  const contents = `The contact with id ${data.id} has been added.`
                  document.querySelector('#result').innerHTML = contents;
              }
              else {
                  const contents=`The user you are trying to add is not registered here or one of you is potentially infected`
                  document.querySelector('#result').innerHTML = contents;
              }
          }

          // Add data to send with request
          const data = new FormData();
          data.append('contact1', contact1);
          data.append('contact2',contact2);

          // Send request
          request.send(data);
          return false;
      };

  });
