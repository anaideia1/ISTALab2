<template>
  <div class="coutries">
    <img alt="Vue logo" src="../assets/authors.png" width = '180' height="130">
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Biography</th>
          <th>City</th>
          <th>Remove</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="author in authors" :key="author.id">
          <td>{{ author.name }}</td>
          <td>{{ author.biography }}</td>
          <td>{{ cities.find(c => c.id = author.city).name }}</td>
          <td><button @click="removeAuthor(author)">-</button></td>
        </tr>
      </tbody>
    </table>
    <br><hr><br>
    <input placeholder="name" v-model="currentAuthor.name">
    <input placeholder="biography" v-model="currentAuthor.biography">
    <select v-model="currentAuthor.city">
      <option disabled value="">Выберите один из вариантов</option>
      <option v-for="city in cities" :key="city.id" :value="city.id" >
        {{city.name}}
      </option>
    </select>
    <button @click="createAuthor()"> Create </button>
  </div>
</template>
<script>
export default {
  name: 'authors',
  data() {
    return {
      authors: [],
      cities: [],
      currentAuthor: {
        name: '',
        biography: '',
        city: null,
      },
    };
  },
  async created() {
    await this.fetchCities();
    await this.fetchAuthors();
  },
  methods: {
    async fetchCities() {
      const response = await fetch('http://localhost:8000/api/v1/cities/');
      this.cities = await response.json();
    },
    async fetchAuthors() {
      const response = await fetch('http://localhost:8000/api/v1/authors/');
      this.authors = await response.json();
    },

    async createAuthor() {
      const response = await fetch('http://localhost:8000/api/v1/authors/', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.currentAuthor),
      });

      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchAuthors();
    },

    async removeAuthor(author) {
      const { id } = author;
      const response = await fetch(`http://localhost:8000/api/v1/authors/${id}`, {
        method: 'DELETE',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
      });

      if (response.status !== 204) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchAuthors();
    },
  },
};
</script>
