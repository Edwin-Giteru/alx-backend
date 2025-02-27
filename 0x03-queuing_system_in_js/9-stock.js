const express = require("express");
const redis = require("redis");
const {promisify} = require("util")
const app = express();
const client = redis.createClient();

 const listProducts = [
    {id: 1, "name": "Suitcase 250", "Price": 50, "stock": 4},
    {id: 2, "name": "Suitcase 450", "Price": 100, "stock": 10},
    {id: 3, "name": "Suitcase 650", "Price": 350, "stock": 2},
    {id: 4, "name": "Suitcase 1050", "Price": 550, "stock": 5},
];

export default function getItemById(id) {
    return listProducts.find(item => item.id === id);
}
app.listen(1245, ()=> {
    console.log("App listening from port: 1245....")
})
app.get("/list_products", (req, res)=> {
    return res.send.json(listProducts);
});
client.on("connect", () => {
    console.log("client connected to server....")
});
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

async function reserveStockById(itemId, stock) {
    return await setAsync(itemId, stock);
}
async function getCurrentReservedStockById(itemId) {
    try {
        const reply = await getAsync(itemId); 
        return reply;
    } catch (error) {
        throw new Error("Error retrieving the item", error);
    }      
}
app.get("/list_products/:itemId", async(req, res) => {
    const itemId = req.params.itemId
    try {
        const item = await getCurrentReservedStockById(itemId);
        return res.json({itemId: item.Id, itemName: item.name, price: item.price, initialAvailableQuantity: item.stock});
    } catch (err) {
        return res.json({status: 'Product not found'});
    }
    
});
app.get("/reserve_product/:itemId", async(req, res) => {
    const itemId = req.params.itemId;
    try {
        const item = await getCurrentReservedStockById(itemId)
        if (item.stock >= 1) {
            await reserveStockById(item.id, item.stock);
            return res.json({status: "Reservation confirmed",itemId: item.id})
        } else {
            return res.json({status: "Not enough stockavailable", itemId: item.id})
        }
    } catch(err) {
        return res.json({status: "Product not found"})
    }

})