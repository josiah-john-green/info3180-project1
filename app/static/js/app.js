document.addEventListener('DOMContentLoaded', function() {
  
  /* Script: Flash Exit */

  // Get the close button for the flash message
  const closeButton = document.getElementById('close-flash');

  // Add click event listener to the close button
  closeButton.addEventListener('click', function() {
      // Find the flash message div and hide it
      const flashMessage = document.getElementById('flash-msg');
      flashMessage.style.display = 'none';
  });

  /* Script: Files */

  document.getElementById('file-upload').addEventListener('change', function() {

    var fullPath = this.value;
    var fileName = fullPath.split('\\').pop();

    // Display the selected file name (optional)
    
    document.getElementById('selected-file').innerHTML = fileName;
  
  });
  
}); 