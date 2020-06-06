<template>
  <div class="coutries">
    <img alt="Vue logo" src="../assets/cities.png" width = '180' height="130">
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Country</th>
          <th>Remove</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="city in cities" :key="city.id">
          <td>{{ city.name }}</td>
          <td>{{ countries.find(c => c.id = city.country).name }}</td>
          <td><button @click="removeCity(city)">-</button></td>
        </tr>
      </tbody>
    </table>
    <br><hr><br>
    <input placeholder="name" v-model="currentCity.name">
    <select v-model="currentCity.country">
      <option disabled value="">Выберите один из вариантов</option>
      <option v-for="country in countries" :key="country.id" :value="country.id" >
        {{country.name}}
      </option>
    </select>
    <button @click="createCity()"> Create </button>
  </div>
</template>
<script>
export default {
  name: 'cities',
  data() {
    return {
      cities: [],
      countries: [],
      currentCity: {
        name: '',
        country: null,
      },
    };
  },
  async created() {
    await this.fetchCities();
    await this.fetchCountries();
  },
  methods: {
    async fetchCities() {
      const response = await fetch('http://localhost:8000/api/v1/cities/');
      this.cities = await response.json();
    },
    async fetchCountries() {
      const response = await fetch('http://localhost:8000/api/v1/countries/');
      this.countries = await response.json();
    },

    async createCity() {
      const response = await fetch('http://localhost:8000/api/v1/cities/', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.currentCity),
      });

      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchCities();
    },

    async removeCity(city) {
      const { id } = city;
      const response = await fetch(`http://localhost:8000/api/v1/cities/${id}`, {
        method: 'DELETE',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
      });

      if (response.status !== 204) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchCities();
    },
  },
};
</script>
