<template>
  <div class="countries">
    <img alt="Vue logo" src="../assets/countries.png" width = '180' height="130">
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Remove</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="country in countries" :key="country.id">
          <td>{{ country.name }}</td>
          <td><button @click="removeCountry(country)">-</button></td>
        </tr>
      </tbody>
    </table>
    <br><hr><br>
    <input placeholder="Name" v-model="currentCountry.name">
    <button @click="createCountry()"> Create </button>
  </div>
</template>
<script>
export default {
  name: 'countries',
  data() {
    return {
      countries: [],
      currentCountry: {},
    };
  },
  async created() {
    await this.fetchCountries();
  },
  methods: {
    async fetchCountries() {
      const response = await fetch('http://localhost:8000/api/v1/countries/');
      this.countries = await response.json();
    },

    async createCountry() {
      const response = await fetch('http://localhost:8000/api/v1/countries/', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.currentCountry),
      });

      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchCountries();
    },

    async removeCountry(country) {
      const { id } = country;
      console.log(id);
      const response = await fetch(`http://localhost:8000/api/v1/countries/${id}`, {
        method: 'DELETE',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
      });

      if (response.status !== 204) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchCountries();
    },
  },
};
</script>
