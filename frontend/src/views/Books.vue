<template>
  <div class="books">
    <img alt="Vue logo" src="../assets/book.png" width = '180' height="130">
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
          <th>Description</th>
          <th>Genre</th>
          <th>Author</th>
          <th>Remove</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="book in books" :key="book.id">
          <td>{{ book.name }}</td>
          <td>{{ book.price }}</td>
          <td>{{ book.description }}</td>
          <td>{{ genres.find(g => g.id = book.genre).name }}</td>
          <td>{{ authors.find(a => a.id = book.author).name }}</td>
          <td><button @click="removeBook(book)">-</button></td>
        </tr>
      </tbody>
    </table>
    <br><hr><br>
    <input placeholder="name" v-model="currentBook.name">
    <input placeholder="price" v-model.number="currentBook.price">
    <input placeholder="description" v-model="currentBook.description">
    <select v-model="currentBook.genre">
      <option disabled value="">Выберите один из вариантов</option>
      <option v-for="genre in genres" :key="genre.id" :value="genre.id" >
        {{genre.name}}
      </option>
    </select>
    <select v-model="currentBook.author">
      <option disabled value="">Выберите один из вариантов</option>
      <option v-for="author in authors" :key="author.id" :value="author.id" >
        {{author.name}}
      </option>
    </select>
    <button @click="createBook()"> Create </button>
  </div>
</template>

<script>
export default {
  name: 'cities',
  data() {
    return {
      books: [],
      authors: [],
      genres: [],
      currentBook: {
        name: '',
        price: '',
        description: '',
        author: null,
        genre: null,
      },
    };
  },
  async created() {
    await this.fetchBooks();
    await this.fetchAuthors();
    await this.fetchGenres();
  },
  methods: {
    async fetchBooks() {
      const response = await fetch('http://localhost:8000/api/v1/books/');
      this.books = await response.json();
    },
    async fetchAuthors() {
      const response = await fetch('http://localhost:8000/api/v1/authors/');
      this.authors = await response.json();
    },
    async fetchGenres() {
      const response = await fetch('http://localhost:8000/api/v1/genres/');
      this.genres = await response.json();
    },

    async createBook() {
      const response = await fetch('http://localhost:8000/api/v1/books/', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.currentBook),
      });

      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchBooks();
    },

    async removeBook(book) {
      const { id } = book;
      const response = await fetch(`http://localhost:8000/api/v1/books/${id}`, {
        method: 'DELETE',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
      });

      if (response.status !== 204) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchBooks();
    },
  },
};
</script>
