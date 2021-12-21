<template>
    <div>
      <section>
			<div class="containers">
				<div class="logindiv center-block mt40">
					<h3>가입하기</h3>
																<!-- 체크박스 -->
						<div class="join-uptext">👋여행가고 싶은 국가(도시) 3개를 선택해주세요!👋</div>
						<p>✈️선택한 순서대로 순위가 정해집니다(3개)✈️</p>
						<p>✅세개 나라를 선택한 후 "확정" 을 눌러주세요✅</p>
						<div style="font-size:14px; algin-items: center;">
							<input type="checkbox" id="브라질" value="Brazil" v-model="preference"> <label for="브라질">브라질</label><img src="https://img.icons8.com/emoji/20/000000/brazil-emoji.png"/>
							<input type="checkbox" id="콜롬비아" value="Colombia" v-model="preference"> <label for="콜롬비아">콜롬비아</label><img src="https://img.icons8.com/emoji/20/000000/colombia-emoji.png"/>
							<input type="checkbox" id="멕시코" value="Mexico" v-model="preference"> <label for="멕시코">멕시코</label><img src="https://img.icons8.com/emoji/20/000000/mexico-emoji.png"/>
							<input type="checkbox" id="라스베이거스" value="LA" v-model="preference"> <label for="라스베이거스">라스베이거스</label><img src="https://img.icons8.com/emoji/20/000000/united-states-emoji.png"/><br>
							<input type="checkbox" id="워싱턴" value="Washington" v-model="preference"> <label for="워싱턴">워싱턴</label><img src="https://img.icons8.com/emoji/20/000000/united-states-emoji.png"/>
							<input type="checkbox" id="시카고" value="Chicago" v-model="preference"> <label for="시카고">시카고</label><img src="https://img.icons8.com/emoji/20/000000/united-states-emoji.png"/>
							<input type="checkbox" id="캐나다" value="Canada" v-model="preference"> <label for="캐나다">캐나다</label><img src="https://img.icons8.com/emoji/20/000000/united-states-emoji.png"/>
							<input type="checkbox" id="칠레" value="Chile" v-model="preference"> <label for="칠레">칠레</label><img src="https://img.icons8.com/emoji/20/000000/chile-emoji.png"/><br>
							<input type="checkbox" id="일본" value="Japan" v-model="preference"> <label for="일본">일본</label><img src="https://img.icons8.com/emoji/20/000000/japan-emoji.png"/>
							<input type="checkbox" id="홍콩" value="Hongkong" v-model="preference"> <label for="홍콩">홍콩</label><img src="https://img.icons8.com/emoji/20/000000/hong-kong-sar-china-emoji.png"/>
							<input type="checkbox" id="중국" value="China" v-model="preference"> <label for="중국">중국</label><img src="https://img.icons8.com/emoji/20/000000/china-emoji.png"/>
							<input type="checkbox" id="인도" value="India" v-model="preference"> <label for="인도">인도</label><img src="https://img.icons8.com/emoji/20/000000/india-emoji.png"/><br>
							<input type="checkbox" id="호주" value="Australia" v-model="preference"> <label for="호주">호주</label><img src="https://img.icons8.com/emoji/20/000000/australia-emoji.png"/>
							<input type="checkbox" id="뉴질랜드" value="NewZleand" v-model="preference"> <label for="뉴질랜드">뉴질랜드</label><img src="https://img.icons8.com/emoji/20/000000/new-zealand-emoji.png"/>
							<input type="checkbox" id="영국" value="UK" v-model="preference"> <label for="영국">영국</label><img src="https://img.icons8.com/emoji/20/000000/united-kingdom-emoji.png"/>
							<input type="checkbox" id="프랑스" value="France" v-model="preference"> <label for="프랑스">프랑스</label><img src="https://img.icons8.com/emoji/20/000000/france-emoji.png"/><br>
							<input type="checkbox" id="이탈리아" value="Italy" v-model="preference"> <label for="이탈리아">이탈리아</label><img src="https://img.icons8.com/emoji/20/000000/italy-emoji.png"/>
							<input type="checkbox" id="남아프리카공화국" value="SouthAfrica" v-model="preference"> <label for="남아프리카공화국">남아공</label><img src="https://img.icons8.com/emoji/20/000000/south-africa-emoji.png"/>
							<input type="checkbox" id="소말리아" value="Somalia" v-model="preference"> <label for="소말리아">소말리아</label><img src="https://img.icons8.com/emoji/20/000000/somalia-emoji.png"/>
							<input type="checkbox" id="모로코" value="Moroco" v-model="preference"> <label for="모로코">모로코</label><img src="https://img.icons8.com/emoji/20/000000/morocco-emoji.png"/>
							<p>❗❗선호도 순위❗❗</p>
							<p>1️⃣: {{ preference[0] }}</p>
							<p>2️⃣: {{ preference[1] }}</p>
							<p>3️⃣: {{ preference[2] }}</p>
							선택한 국가(도시) 수: {{this.preference.length }}개 <b-button pill variant="outline-info" @click="che()">확정</b-button>
						</div>
						<div class="the_line"></div>
					<form name="loginform">
						<div class="join-uptext">아이디</div>
						<div class="login-info-div">
							<input type="text" name="username" id="username" v-model="credentials.username" placeholder="아이디는 영문 대소문자 5~15자 이내로 생성 가능합니다." >
							<span id="msg1" style="color:#f00"></span>
						</div>
						<!-- 닉네임 추가 -->
						<div class="join-uptext">닉네임</div>
						<div class="login-info-div">
							<input type="text" name="nickname" id="nickname" v-model="credentials.nickname" placeholder="닉네임은 영문 대소문자 5~15자 이내로 생성 가능합니다." >
							<span id="msg2" style="color:#f00"></span>
						</div>
						<!--  -->
						<div class="join-uptext">비밀번호</div>
						<div class="login-info-div">
							<input type="password" name="pw" id="pw" v-model="credentials.password" placeholder="비밀번호는 영문 대소문자 8~15자 이내로 생성 가능합니다.">
							<span id="msg3" style="color:#f00"></span>
						</div>
						<div class="login-info-div">
							<input type="password" name="pw2" id="pw2" v-model="credentials.passwordConfirmation" placeholder="비밀번호를 확인합니다">
							<span id="msg4" style="color:#f00"></span>
						</div>






						<!-- 이메일 X -->
						<!-- <div class="join-uptext">이메일</div>
						<div class="login-info-div">
							<input type="email" name="email" id="email" v-model="credentials.email" placeholder="사용하실 이메일을 입력해주세요">
							<span id="msg5" style="color:#f00"></span>
						</div> -->
						<div class="">
							<label for="allcheck" class="pointer join-checkbox-label pull-left">
								<input id="allcheck" type="checkbox" name="allcheck"><span>전체 동의</span>
							</label>
							<div class="clearfix"></div>
						</div>
						<div class="the_line"></div>
						<div class="join-checkbox">
							<ul class="list-unstyled">
								<li>
									<label for="ok" class="pointer join-checkbox-label pull-left">
										<input id="ok" type="checkbox" name="ok"><span>  이용 약관 동의</span>
									</label>
									<div class="pull-right">
										<a id="ok-btn" class="pointer">내용보기</a>
									</div>
									<div class="clearfix"></div>
								</li>
								<li>
									<label for="ok2" class="pointer join-checkbox-label pull-left">
										<input id="ok2" type="checkbox" name="ok2"><span>개인 정보 수집,이용 동의</span>
									</label>
									<div class="pull-right">
										<a id="ok2-btn" class="pointer">내용보기</a>
									</div>
									<div class="clearfix"></div>
								</li>
								<li>
									<label for="ok3" class="pointer join-checkbox-label pull-left">
										<input id="ok3" type="checkbox" name="ok3"><span>만 14세 이상입니다.</span>
									</label>
									<div class="clearfix"></div>
								</li>
							</ul>
						</div>
						<div class="login-submit-div mt40">
							<a onclick="goJoin()" @click="signup" class="pointer">가입하기</a>
						</div>
					</form>





					<div class="mt10 small-join">
						<span>이미 계정이 있다면? <router-link :to="{ name: 'Login' }">로그인하러가기</router-link></span>
					</div>
				</div>
			</div>
		</section>
		
		<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
			<div class="modal-dialog" >
				<div class="modal-content">
					<div class="modal-header">
						<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
						<h4 class="modal-title" id="myModalLabel"></h4>
					</div>
					<div class="modal-body" style="overflow:hidden;">
					</div>
					<div class="modal-footer">
						<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
					</div>
				</div>
			</div>
		</div>
    </div>
</template>
<script>
import axios from 'axios'
import 'bootstrap'
// npm i vue-swal 필요
import swal from "sweetalert";

// import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
// npm update vue-template-compiler 필요

export default {
  name: 'Signup',
  data: function () {
		return {
			preference: [],
			credentials: {
				username: null,
				nickname: null,
        password: null,
        passwordConfirmation: null,
				user_preference: '',
      }
    }
  },
  methods: {
		che: function () {
			for (let a = 0; a < this.preference.length; a++) {
				this.credentials.user_preference += this.preference[a]
				this.credentials.user_preference += '.'
				console.log(this.credentials.user_preference)
			}
		},
		refreshPreference: function () {
			this.credentials.user_preference = ''
		},
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
        .then(() => {
          this.$router.push({ name: 'Login'})
        })
				// back에서 확인후 가져온 에러로 팝업창 띄우기
        .catch(err => {
					// console.log(err.response)
          swal(err.response.data.error, {
            dangerMode: true,
          }),
					this.refreshPreference()
      })
    },
		watch: {
			preference: function () {
				if (this.preference.length > 3) {
					alert('3가지 국가(도시)를 선택했는지 다시 확인해주세요😫')
					this.preference=[]
					this.credentials.user_preference = ''
			}
			}
		}
	},
	// computed: {
  //   preference: function () {
  //     return this.credentials.user_preference += this.preference[this.preference.length -1]
  //   }
  // },
}
</script>

<style scoped>
.containers {
	width:80%;
	margin:auto;
}
</style>
<style scoped>
html {
	background: #37373d;
}
body {
	background: #37373d;
}
#app {
	background: #37373d;
}
section {
  height:1400px;
	background: #37373d;
}
</style>
