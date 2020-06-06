<template>
  <div id="app">
    <div id="nav">
      <router-link to="/genres"> Genres </router-link> |
      <router-link to="/"> Books </router-link> |
      <router-link to="/authors"> Authors </router-link> |
      <router-link to="/cities"> Cities </router-link> |
      <router-link to="/countries"> Countries </router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

table{
  margin: auto;
  border-spacing: 20px 10px;
}
</style>
