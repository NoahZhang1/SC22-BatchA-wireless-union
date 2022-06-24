# Wireless Wingman
# ![](wireless_wingman.png)


<a href="https://github.com/Mindstormer314/AI-Camp-Data/tree/main/Copilot"><img src="https://img.shields.io/badge/dataset-download-green" alt="Contributions welcome" data-canonical-src="https://img.shields.io/badge/dataset-download-green" style="max-width:100%;"></a> <a href="https://opensource.org/licenses/apache" rel="nofollow"></a>

<a href="https://drive.google.com/drive/folders/1-H_AeVwm7lJxVTs-c4kwzRtMvXlNGUTC"><img src="https://img.shields.io/badge/model-download-blue" alt="Contributions welcome" data-canonical-src="https://img.shields.io/badge/dataset-download-green" style="max-width:100%;"></a> <a href="https://opensource.org/licenses/apache" rel="nofollow"></a>

#### The Wireless Wingman is designed to take a simple prompt and to expand on that. With dataset scraped from [The Algorithm] repository (https://github.com/TheAlgorithms), our model does not only trained with pre-written algorithm but also mimic the coding style written by professional programmers. The [pre-trained GPT-2 variants](https://huggingface.co/transformers/pretrained_models.html) are offered by the awesome [🤗 transformers](https://github.com/huggingface/transformers) library and [tenserflow] (https://www.tensorflow.org/).


### Features
- Generate code written in Python, Java, JavaScript, C, C++ and C#

### Files and Directories:

The architecture of files and directories are as follows:

* app/
	* model/
		* *EMITTED*
	*	static/
		*	css/
		*	img/
		* js/
		* favicon.ico	
	*	templates/
		*	C-Popup.html
        *	Cpp-Popup.html
        *	CS-Popup.html
        *	index.html
        *	Java-Popip.html
        *	JS-Popup.html
        *	Python-Popup.html
        *	writer_home.html
        *	write-your-code-with-AI.html
	*	main.py
    *	popup_main.py
	*	requirements.txt
	*	utils.py
* .gitignore
* Dockerfile
* Readme.md
* config.py
* entrypoint.sh
* host_config
* nginx_host


### Quick Start
Here provides three ways of quick-start. Before that,


#### Example Code Generation Process
`pip install aitextgen`
`pip install transformer`


```python
# import stuff for our web server
from flask import Flask, request, redirect, url_for, render_template, session
from utils import get_base_url
# import stuff for our models
from aitextgen import aitextgen
from transformers import PreTrainedTokenizerFast, GPT2DoubleHeadsModel, GPT2TokenizerFast, GPT2Tokenizer


def load_model(model_path):
    model = GPT2DoubleHeadsModel.from_pretrained(model_path)
    return model


def load_tokenizer(tokenizer_path):
    tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path)
    return tokenizer

#For generating language from any existing model
def GenAI_JS(): 

    model = load_model("model/js")
    tokenizer = load_tokenizer("model/js")
    if prompt is not None:
        generated = model.generate(
            ids,
            do_sample=True,
            max_length=150,
            pad_token_id=model.config.eos_token_id,
            top_k=50,
            top_p=0.95,
            return_as_list=True
        )
    generated = tokenizer.decode(generated[0], skip_special_tokens=True)
```



### Generative examples

```C++
-------------Example 1--------------------------------------
Context code: void Dijkstra
Generated: 

void Dijkstra(double B, double B2, double B2,
                              int limit1 = 10) {
        this->m = B[0].size();
        this->prev = B[0].top().second;
    }
}

int main() {
    std::srand(std::time(nullptr));
    test();
    return 0;
}

#include <cmath>
#include <iostream>

--------------Example 2-------------------------------------
```C
Context code: int bubbleSort(arr)
Generated:
int bubbleSort(arr)
{
    for (int i = 0; i < array->size; i++)
    {
        assert(array->array[i] <= array->array[i - 1]);
    }

    free(arr);
}


int main()
{
    test();
    return 0;
}


```
