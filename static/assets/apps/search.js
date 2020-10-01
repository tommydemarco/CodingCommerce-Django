new Vue({
  el: 'app',
  delimiters: ['{$', '$}'],

  //
  mounted() {
    var self = this;
    // cargamos lista de personas
    axios.get('api/products/list/')
      .then(function (response) {
        self.listaPersonas = response.data;
      })
      .catch(function (error) {
        console.log(error);
      });
  },
  methods: {
    buscar_persona: function(kword){
      var self = this;
      axios.get('api/products/search/<str:kword>' + kword + '/')
        .then(function (response) {
          self.listaPersonas = response.data;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
  watch: {
    kword: function (val) {
      var self = this;
      self.buscar_persona(val)
    },
  },
  data: {
    listaPersonas:[],
    kword:'',
  },
})
