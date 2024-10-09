#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
    let characters_length;
    if (error) {
        console.error('Error:', error);
    } else {
        const data = JSON.parse(body);
        characters_length = data.characters;
        for (const link of characters_length) {
            request(link, (err, response, body) => {
                if (error) {
                    console.error('Error:', error);
                } else {
                    const data = JSON.parse(body);
                    console.log(data.name);
                }
            });
        }
    }
});
