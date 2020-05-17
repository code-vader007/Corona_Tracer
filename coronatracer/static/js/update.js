document.addEventListener('DOMContentLoaded', () => {

      document.querySelector('#update').onsubmit = () => {
        const request = new XMLHttpRequest();
        const color = document.querySelector('#btn').value;
        request.open('POST', '/convert');
          // Callback function for when request completes
          request.open('POST', '/calc');
          request.onreadystatechange = () => {

              // Extract JSON data from request
              const data = JSON.parse(request.responseText);

              // Update the result div
              if (data.success) {
                  const contents = `Your health has been updated to ${data.color}`
                  document.querySelector('#result').innerHTML = contents;
              }
              else {
                  document.querySelector('#result').innerHTML = 'There was an error.';
              }
          }

          // Add data to send with request
          const data = new FormData();
          data.append('color', color);

          // Send request
          request.send(data);
          return false;
      };

  });
