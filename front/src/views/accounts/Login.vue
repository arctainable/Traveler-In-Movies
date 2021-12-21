<template>
  <section>
			<div class="container">
				<div class="logindiv center-block mt40">
					<h3>로그인</h3>
					<form name="loginform" id="loginform">
						<div class="login-info-div">
							<input type="text" name="id" id="username" v-model="credentials.username" placeholder="아이디 입력" >
						</div>
						<div class="login-info-div">
							<input type="password" id="password" v-model="credentials.password" name="pw" placeholder="비밀번호 입력">
						</div>
						<div class="login-submit-div mt40">
							<a @click="login" id="login-btn" class="pointer">로그인</a>
              <!-- google -->
              <div class="g-signin2" id="google-signin-btn" data-onsuccess="onSignIn" data-width="385" data-longtitle="true"></div>
						</div>
					</form>
					<div class="mt10 small-join">
						<span> 계정이 없다면? <router-link :to="{ name: 'Signup' }">가입하러가기</router-link></span>
					</div>
					<div class="the_line"></div>
					<div class="mt10 small-join">
						<span><a href="#">비밀번호를 찾고 계신가요?</a></span>
					</div>
				</div>
			</div>

    <!-- google logout -->
    <!-- <button @click="authInst">logout</button> -->
		</section>
</template>

<script>
import axios from 'axios'
import {mapActions, mapGetters, mapState} from 'vuex'
import swal from 'sweetalert'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
		...mapActions([
			'loginGetToken',
      'getProfile',
      'getReviewsGenre',
      'getReviewsCountry',
      'getReviews',
      'getReviewsMovieInfo',
      'getReviewsMovieGenreCountry',
		]),
    // google
    onSignIn(googleUser){
      const profile = googleUser.getBasicProfile();
      console.log('ID Token: ', googleUser.getAuthResponse().id_token)
      console.log('Name: ' + profile.getName())
    },
    signout() {
      const authInst = window.gapi.auth2.getAuthInstance();
      // eslint-disable-next-line
      console.log(authInst);
    },

    isValid: function () {

      if (this.credentials.username === '') {
        swal ('아이디를 입력하세요.', {
          dangerMode: true,
        })
      } else if (this.credentials.password === '') {
        swal ('비밀번호를 입력하세요.', {
          dangerMode: true,
        })
      } else {
        this.login()
      }
    },

    login: function () {
      
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials
        })
        .then(res => {
          console.log(this.credentials)
          localStorage.setItem('jwt', res.data.token)
          localStorage.setItem('username', this.credentials.username)
          this.$emit('login')
          this.loginGetToken()
          // this.setToken()
          this.getProfile()
          console.log('userid', this.userid)
          this.getReviewsGenre()
          this.getReviewsCountry()
          this.getReviews()
          this.getReviewsMovieInfo()
          this.getReviewsMovieGenreCountry()
          this.$router.push({ name: 'Home' })
          // commit("SET_TOKEN", res.data.token)
          
        })
        .catch(err => {
          swal ('회원 정보가 일치하지 않습니다.', {
          dangerMode: true,
        })
          console.log(err)
        })
      }
  
  },
  computed: {
    ...mapGetters([
      'getUserid'
    ]),
    ...mapState([
      'userid'
    ])

  },
  created(){
    window.onSignIn = this.onSignIn
  },
  // updated: function () {
  //   this.getProfile()
  // }
}
</script>
<style scoped>
section {
  min-height:900px;
}
</style>
