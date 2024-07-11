#!/usr/bin/node
/**
* Stars Wars Characters
*/
const request = require('request');

const id = process.argv[2];
const endpoint = `https://swapi-api.alx-tools.com/api/films/${id}/`;

function getCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, response, body) => {
      if (err) {
        reject(err);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch character: ${response.statusCode}`));
      } else {
        const data = JSON.parse(body);
        resolve(data.name);
      }
    });
  });
}

request(endpoint, async (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch film:', response.statusCode);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  if (characterUrls) {
    for (const url of characterUrls) {
      try {
        const name = await getCharacter(url);
        console.log(name);
      } catch (error) {
        console.error('Error fetching character:', error);
      }
    }
  }
});
