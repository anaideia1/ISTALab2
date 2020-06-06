<template>
  <div class="genres">
    <img alt="Vue logo" src="../assets/genres.png" width = '180' height="130">
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Remove</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="genre in genres" :key="genre.id">
          <td>{{ genre.name }}</td>
          <td><button @click="removeGenre(genre)">-</button></td>
        </tr>
      </tbody>
    </table>
    <br><hr><br>
    <input placeholder="Name" v-model="currentGenre.name">
    <button @click="createGenre()"> Create </button>
  </div>
</template>
<script>
export default {
  name: 'genres',
  data() {
    return {
      genres: [],
      currentGenre: {},
    };
  },
  async created() {
    await this.fetchGenres();
  },
  methods: {
    async fetchGenres() {
      const response = await fetch('http://localhost:8000/api/v1/genres/');
      this.genres = await response.json();
    },

    async createGenre() {
      const response = await fetch('http://localhost:8000/api/v1/genres/', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.currentGenre),
      });

      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchGenres();
    },

    async removeGenre(genre) {
      const { id } = genre;
      const response = await fetch(`http://localhost:8000/api/v1/genres/${id}`, {
        method: 'DELETE',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
      });

      if (response.status !== 204) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchGenres();
    },
  },
};
</script>
