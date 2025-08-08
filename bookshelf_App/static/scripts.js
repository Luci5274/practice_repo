  function toggleEditForm(index) {
    const form = document.getElementById(`edit-form-${index}`);
    if (form.style.display === 'none') {
      form.style.display = 'block';
    } else {
      form.style.display = 'none';
    }
  }