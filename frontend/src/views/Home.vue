<template>
    <div>
        <el-container>
            <el-header height='40px'>
                <Header :signed="this.signed"/>
            </el-header>
            <el-main>
                <Nav/>
                <div class="card-list">
                    <videoCard  v-for="index of 5" :key="index"/>
                </div>
            </el-main>
            <el-footer height='40px'>
                <Footer/>
            </el-footer>
        </el-container>
    </div>
</template>

<style scoped>
.el-header, .el-footer {
    background-color: #ffffff;
    color: #333;
    line-height: 30px;
  }

  .el-main {
    background-color: #ffffff;
    color: #333;
    width: 76%;
    margin: auto;
  }
  .card-list{
      margin-top: 50px;
  }
</style>

<script>
import Nav from '@/components/Nav'
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import videoCard from '@/components/videoCard'
import Videos from './videos.vue'

export default {
    name :'Home',
    components: { Nav,Header,Footer,Videos,videoCard },

    data(){
        return{
            signed:false,
            video:{}
        }
    },
    created(){
        let token = this.$cookies.get('user');
        if(token){
            this.signed = true;
        }
    }
}

</script>