function displayUploadChanger() {
    const fileInput = document.getElementById('csv-upload');
    const fileNameDisplay = document.getElementById('file-name');
    const uploadIcon = document.getElementById('upload-status-icon');
    const labelBorder = document.getElementById('label-upload-csv');
    const spanText = document.getElementById('span-text');
    const buttonFormCsv = document.getElementById('button-form-csv');


    if (fileInput.files && fileInput.files.length > 0) {
        const fileName = fileInput.files[0].name;
        fileNameDisplay.textContent = `Arquivo selecionado: ${fileName}`;
        fileNameDisplay.classList.add('font-bold', 'text-green-800');
        uploadIcon.classList.remove('text-gray-400');
        uploadIcon.classList.add('text-green-600');
        labelBorder.classList.remove('border-gray-300', 'hover:border-gray-400');
        labelBorder.classList.add('border-green-600', 'hover:border-green-400');
        spanText.textContent = ' ';
        buttonFormCsv.classList.remove('bg-gray-400', 'hover:bg-gray-700');
        buttonFormCsv.classList.add('bg-green-600', 'hover:bg-green-800', 'cursor-pointer');
        
    } else {
        fileNameDisplay.textContent = 'Arraste e solte seu arquivo aqui, ou clique para selecionar um arquivo. Suportado: .csv | Tamanho máximo: 5MB';
        uploadIcon.classList.remove('text-green-600');
        uploadIcon.classList.add('text-gray-400');
        formBoarder.classList.remove('border-green-600');
        formBoarder.classList.add('border-gray-300');
    }
}