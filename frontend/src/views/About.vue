<template>
  <div class="about">
    <h1>{{msg}}</h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'About',
  data() {
    return {
      msg: 'Hello World!',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  }
}
</script>