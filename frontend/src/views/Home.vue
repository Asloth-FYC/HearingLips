<template>
    <div>
        <el-container>
            <el-header height='40px'>
                <Header :signed='signed' :username='username'/>
            </el-header>
            <el-main>
                <Nav/>
                <div class="card-list">
                    <videoCard  v-for="(file,index) in projects" :key="index"
                    :project_name="file.name"
                    :create_at="file.create_at"
                    :url="file.url"/>
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
import { get } from '../api/admin'

export default {
    name :'Home',
    components: { Nav,Header,Footer,videoCard },
    data(){
        return{
            signed:false,
            username:'',
            projects:[]
        }
    },
    created(){
        //验证当前的token是否过期
        get().then(resp=>{
            let data = resp.data;
            if(data.code===200){
                this.signed = true;
                this.username=data.usermsg.username;
                this.projects = data.projects
            }else{
                this.$notify({
                    title: '错误',
                    message: data.msg,
                    type: 'warning'
                });
                this.$router.push('/login');
            }
        })


    }
}

</script>