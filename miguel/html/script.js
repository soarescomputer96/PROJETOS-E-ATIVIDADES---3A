function calcularIMC() {
    const peso = parseFloat(document.getElementById('peso').value);
    const altura = parseFloat(document.getElementById('altura').value);
    
    if (isNaN(peso) || isNaN(altura) || peso <= 0 || altura <= 0) {
        alert('Por favor, insira valores válidos.');
        return;
    }

    const imc = peso / (altura * altura);
    const resultadoElement = document.getElementById('resultado');
    const imcElement = document.getElementById('imc');
    const categoriaElement = document.getElementById('categoria');

    imcElement.textContent = `IMC: ${imc.toFixed(2)}`;

    let categoria = '';

    if (imc < 18.5) {
        categoria = 'Abaixo do peso';
    } else if (imc < 24.9) {
        categoria = 'Peso normal';
    } else if (imc < 29.9) {
        categoria = 'Sobrepeso';
    } else {
        categoria = 'Obesidade';
    }

    categoriaElement.textContent = `Categoria: ${categoria}`;
}
