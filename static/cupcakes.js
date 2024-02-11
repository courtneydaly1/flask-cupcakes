const BASE_URL= 'http://127.0.0.1:5000/api'

function createCupcakeHTML(cupcake) {
    return `
    <div data-cupcake-id='${cupcake.id}'>
    <li>
    ${cupcake.flavor}/${cupcake.size}/${cupcake.rating} 
    <button class='delete-btn'> DELETE </button>
    </li>
    <img class='cupcake-img' src='${cupcake.image}' alt='No image provided'</div>`;
}

async function showCupcakes() {
    const res = await axios.get(`${BASE_URL}/cupcakes`);

    for (let cupcakeData of res.data.cupcakes){
        let newCupcake = $(createCupcakeHTML(cupcakeData));
        $('#cupcake-list').append(newCupcake);
    }
}

$('#cupcake-form').on('submit', async function (e){
    e.preventDefault();

    let flavor= $('#form-flavor').val();
    let size=$('#form-size').val();
    let rating= $('#form-rating').val();
    let image= $('#form-image').val();
    
    const newCupcakeRes= await axios.post(`${BASE_URL}/cupcakes`, {flavor, size, rating, image});

    let newCupcake= $(createCupcakeHTML(newCupcakeRes.data.cupcake));

    $('#cupcake-list').append(newCupcake);
    $('#cupcake-form').trigger('reset');
});

$('#cupcake-list').on('click', ".delete-btn", async function(e){
    e.preventDefault();
    let $cupcake = $(e.target).closest('div');
    let cupcakeID= $cupcake.attr('data-cupcake-id');

    await axios.delete(`${BASE_URL}/cupcakes/${cupcakeID}`);
    $cupcake.remove();
});

$(showCupcakes);