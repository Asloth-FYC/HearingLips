<template>
    <el-dialog
            title="修改密码"
            :visible.sync="dialogVisible"
            :lock-scroll="false"
            width="800px">
        <el-form :model="form" ref="form" size="medium" label-width="80px" :rules="rules">
            <el-form-item label="原密码" prop="inputOpassword" >
                <el-input placeholder="请输入原密码" type="password"
                          v-model="form.inputOpassword"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="inputPassword" :error="errorText">
                <el-input placeholder="设置新密码" type="password" 
                          v-model="form.inputPassword"  @input="onPasswordInput"></el-input>
            </el-form-item>
            <el-form-item label="确认" prop="confirmPassword" :error="errorText">
                <el-input placeholder="确认新密码" type="password"
                          v-model="form.confirmPassword"  @input="onPasswordInput"></el-input>
            </el-form-item>
            <el-form-item class="text-center">
                <el-button type="primary" @click="onConfirm" style="width: 200px">{{btnText2}}</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
    import dialogmixin from "@/assets/js/dialogMixin";
    import { updatePsw } from "@/api/user";
    export default {
        mixins: [dialogmixin],
        data() {
            return {
                form: {},
                errorText: '',
                btnText2:'确认',
                rules,
            }
        },
        methods:{
            onPasswordInput() {
                if (this.form.inputPassword !== this.form.confirmPassword) {
                    this.errorText = '两次密码不一致';
                } else {
                    this.errorText = '';
                }
            },
            onConfirm() {
                this.$refs.form.validate(valid => {
                    if (valid) {
                        if (this.form.inputPassword !== this.form.confirmPassword) {
                            this.message({
                                message: '两次密码不一致',
                                type: 'warning'
                            });
                            return;
                        } else {
                            this.errorText = '';
                        }
                        updatePsw(this.form).then(resp => {
                            let data = resp.data;
                            if(data.code==200){
                                this.$notify({
                                    message: data.msg,
                                    type: 'success'
                                });
                                this.$router.push({name:'login'});
                            }else{
                                this.$notify({
                                    title: '错误',
                                    message: data.msg,
                                    type: 'error'
                                });
                            }
                        })
                    }
                })
            },
        }
    }
    const emptyText="不能为空";
    var emptyValid = msg => {
        return {required: true, message: msg + emptyText, trigger: "blur"};
    };
    const rules = {
        inputOpassword:[emptyValid("原密码")],
        inputPassword: [emptyValid("新密码")],
        confirmPassword: [emptyValid("确认密码")],
    }
</script>
