#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

function getData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`HTTP ${response.statusCode}`));
      } else {
        try {
          resolve(JSON.parse(body));
        } catch (err) {
          reject(err);
        }
      }
    });
  });
}

async function main () {
  const film = await getData(url);

  for (const characterUrl of film.characters) {
    const character = await getData(characterUrl);
    console.log(character.name);
  }
}

main().catch(console.error);
