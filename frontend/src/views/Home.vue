<template>
    <div>
        <el-container>
            <el-header height='40px'>
                <Header :username="this.name"/>
            </el-header>
            <el-main>
                <Nav/>
                <div>视频</div>
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
    text-align: center;
    line-height: 550px;
  }
</style>

<script>
import Nav from '@/components/Nav'
import Header from '@/components/Header'
import Footer from '@/components/Footer'
export default {
    name :'Home',
    components: { Nav,Header,Footer },
    data(){
        return{
            name:this.$route.params.name,
            video:{}
        }
    },
}

</script>