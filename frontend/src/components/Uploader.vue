<template>
  <div class="uploadBox">
    <el-upload
        class="upload-demo"
        ref="upload"
        drag
        :auto-upload="false"
        list-type="picture"
        :file-list="fileList"
        action="https://jsonplaceholder.typicode.com/posts/"
        multiple>
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
    </el-upload>
    <el-button class="submit" size="small"  @click="submitUpload">submit   </el-button>
  </div>
</template>

<script>
export default {
    name:'Uploader',
  data(){
    return{
      fileList:[],
      filename:''
    }
  },
  methods:{
    submitUpload: function () {
      this.$refs.upload.submit()
    },
  },

}
</script>

<style scoped>
.uploadBox{
  width: auto;
  height: auto;
  padding-left: 2%;
  padding-right: 2%;
  padding-top: 4%;
  padding-bottom: 4%;
  background-color: white;

  position: fixed;
  top:20%;
  left: 30%;

  border-color: #393939;
  border-style: dashed;
  border-width: 0.8px;

  font-family: 'Montserrat', sans-serif;
  font-size: 12px;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.upload-demo{
  align-self: center;
}
.submit{
  margin-top: 5%;
  width:20%;
  font-size: 16px;
}
.submit:hover {
  background-color: #ccc;
  box-shadow: 0px 15px 20px rgba(172, 182, 178, 0.4);
  color: #fff;
  transform: translateY(-4px);
}
</style>