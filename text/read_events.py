import argparse
import tensorflow as tf




def print_event(event_file):
    for e in tf.compat.v1.train.summary_iterator(event_file):
        print("Step: ", e.step)
        for v in e.summary.value:

            # if v.tag == 'eval_classify_loss' or v.tag == 'eval_classify_accuracy':
            #     print(v.simple_value)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', "--event_file", required=True)
    args = parser.parse_args()

    print_event(args.event_file)