
async function fetchData(name) {

    try {

        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${name}`);

        if(!response.ok) {
            throw new Error('Could not fetch resource');
        }

        const data = await response.json();
        return data;
        

    } catch (error) {
        console.error(error);
    }

}

const button = document.getElementById('fetchPokemon');
const image = document.getElementById('pokemonImage');

button.addEventListener('click', async function(){

    const pokemon = document.getElementById('pokemon').value.toLowerCase();
    const data = await fetchData(pokemon)
    image.src = data.sprites.front_default;
    image.style.display = 'block'


});
