<template>
<div>
    <div>
        <router-link to="/">
            <strong style="font: italic 1.3em Georgia, serif;">HearingLips</strong>
        </router-link>
        <el-dropdown>
            <el-button icon="el-icon-user" circle></el-button>
            <el-dropdown-menu slot="dropdown">
                <router-link to="/profile/index">
                <el-dropdown-item >
                    <span>Signed in as</span>
                    <strong style="display:block;">{{this.username}}<i class="el-icon-edit"></i></strong>
                </el-dropdown-item>
                </router-link>
            <router-link to="/">
                <el-dropdown-item divided>项目介绍</el-dropdown-item>
            </router-link>
            <a target="_blank" href="https://github.com/Asloth-FYC/HearingLips">
                <el-dropdown-item>Github</el-dropdown-item>
            </a>
            <el-dropdown-item divided @click.native="logout">
                <span style="display:block;">退出登录</span>
            </el-dropdown-item>
            </el-dropdown-menu>
        </el-dropdown>
    </div>
</div>
    
</template>

<style scoped>
.el-dropdown {
    vertical-align: top;
    position: absolute;
    right: 20px;
}
a {
  text-decoration: none;
}

</style>

<script>
export default {
    name:'Header',
    props:{
        username:String
    },
    methods:{
        logout() {
            this.$router.push({name:'login'})
        }
    },
}
</script>