<template>
  <div class="about">
    <h1>
      {{msg}}
    </h1>
  </div>
</template>

<script>
import {helloFlask} from '../api/helloFlask'
export default {
  name: 'About',
  data(){
    return {
      msg:''
    }
  },
  created(){
    helloFlask().then(resp=>{
      this.msg = resp.data;
    })
  }
}
</script>