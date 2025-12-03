function displayUploadChanger() {
    const fileInput = document.getElementById('csv-upload');
    const label = document.getElementById('label-upload-csv');
    const fileNameDisplay = document.getElementById('file-name');
    const wrapper = document.getElementById('button-box');

    if (fileInput.files?.length > 0) {
        const fileName = fileInput.files[0].name;
        fileNameDisplay.textContent = `Arquivo selecionado: ${fileName}`;

        label.classList.remove("is-default");
        label.classList.add("is-uploaded");
        wrapper.classList.remove("is-default");
        wrapper.classList.add("is-uploaded");
    } else {
        fileNameDisplay.textContent = 'Nenhum arquivo selecionado';

        label.classList.remove("is-uploaded");
        label.classList.add("is-default");
        wrapper.classList.remove("is-uploaded");
        wrapper.classList.add("is-default");
    }
}
