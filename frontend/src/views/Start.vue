<template>
    <div>
        <Header/>
        <div class="step">
            <el-steps :active="activeStep" finish-status="success" simple style="margin-top: 20px">
                <el-step title="提交视频" ></el-step>
                <el-step title="等待机翻" ></el-step>
                <el-step title="查看结果" ></el-step>
                <el-step title="在线校译" ></el-step>
                <el-step title="导出字幕" ></el-step>
            </el-steps>
        </div>


        <div class="form">
            <el-form label-position="top" :model="postPrams" :rules="rules" ref="ruleForm">
                <el-form-item label="项目名称" prop="name">
                    <el-input v-model="postPrams.name" maxlength="10" show-word-limit></el-input>
                </el-form-item>
                <el-form-item label="翻译类型" prop="type">
                    <el-select v-model="postPrams.type" placeholder="请选择翻译类型">
                        <el-option label="唇语识别" value="1"></el-option>
                        <el-option label="语音翻译" value="2"></el-option>
                    </el-select>
                </el-form-item>
                <div class="uploadBox">
                    <el-upload
                    class="upload-demo"
                    ref="upload"
                    drag
                    :data="postPrams"
                    :auto-upload="false"
                    list-type="picture"
                    :file-list="fileList"
                    action="http://localhost:5000/upload"
                    :on-success="handleSuccess"
                    :on-error="handleError"
                    multiple>
                <i class="el-icon-upload"></i>
                <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                </el-upload>
                <el-button class="submit" type="primary" plain icon="el-icon-check" circle @click="submitUpload('ruleForm')"></el-button>
                </div>
            </el-form>
        </div>
    </div>
</template>
<style scoped>
.step{
    padding-top: 30px;
    margin:auto;
    width: 60%;
}
.form{
    width: 30%;
    margin:auto;
    margin-top: 30px;
}
.uploadBox{
  width: auto;
  height: auto;
  padding-top: 8%;
  background-color: white;
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
  font-size: 16px;
}
.submit:hover {
  background-color: rgb(72, 172, 202);
  box-shadow: 0px 15px 20px rgba(252, 197, 249, 0.4);
  color: #fff;
  transform: translateY(-4px);
}

</style>
<script>
import Header from '../components/Header.vue'
export default {
    name:'Start',
    components: {Header},
    data() {
      return {
        postPrams:{
          name: '',
          type: ''
        },
        fileList:[],
        activeStep:0,
        rules: {
          name: [
            { required: true, message: '请输入项目名称', trigger: 'blur' },
          ],
          type: [
            { required: true, message: '请选择翻译类型', trigger: 'change' }
          ],
        }
      };
    },
    methods: {
        submitUpload: function (formName) {
          this.$refs[formName].validate((valid) => {
            if (valid) {
              this.$refs.upload.submit()
            } else {
              console.log('error submit!!');
              return false;
            }
          });
        },
        handleSuccess(){
          this.$notify({
            title: '文件上传成功',
            type: 'success'
          });
          this.activeStep = 1;
          console.log(this.fileList);
        },
        handleError(){
          this.$notify({
            title: '错误',
            message:'文件上传失败，请稍后再试',
            type: 'error'
          });
        }
    }
}

</script>