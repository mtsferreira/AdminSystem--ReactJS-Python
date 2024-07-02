export async function searchCEP(cep) {
    try {
        const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
        
        if (!response.ok) {
            alert('Não foi possível obter os dados');
        }

        const dados = await response.json();

        return {city: dados.localidade, uf: dados.uf, street: dados.logradouro, district: dados.bairro, ibge: dados.ibge, error: dados.erro}
    } catch (error) {
        return error
    }
}